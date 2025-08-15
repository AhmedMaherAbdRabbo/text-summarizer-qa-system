from flask import Flask, request, jsonify, render_template
from transformers import pipeline
import re
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

print("Loading summarization model...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", framework="pt")

print("Loading QA model...")
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2", framework="pt")

def split_text_into_chunks(text, max_chunk_size=1000):
    sentences = re.split(r'[.!?]+', text)
    chunks, current_chunk = [], ""
    for sentence in sentences:
        if len(current_chunk) + len(sentence) < max_chunk_size:
            current_chunk += sentence + ". "
        else:
            if current_chunk.strip():
                chunks.append(current_chunk.strip())
            current_chunk = sentence + ". "
    if current_chunk.strip():
        chunks.append(current_chunk.strip())
    return chunks

def merge_summaries(summaries):
    combined_text = " ".join(summaries)
    if len(combined_text) > 1000:
        return summarizer(combined_text, max_length=200, min_length=50, do_sample=False)[0]['summary_text']
    return combined_text

def summarize_text(text, max_length=150, min_length=30):
    text = text.strip()
    if len(text) < 50:
        return "Text is too short for summarization."
    if len(text) <= 1000:
        summary = summarizer(text, max_length=max_length, min_length=min_length, do_sample=False)
        return summary[0]['summary_text']
    chunks = split_text_into_chunks(text, max_chunk_size=900)
    summaries = []
    for chunk in chunks:
        if len(chunk.strip()) >= 50:
            chunk_summary = summarizer(chunk, max_length=100, min_length=20, do_sample=False)
            summaries.append(chunk_summary[0]['summary_text'])
    return merge_summaries(summaries)

def answer_question(question, context):
    context = context.strip()
    if len(context) <= 1000:
        result = qa_pipeline(question=question, context=context)
        return {'answer': result['answer'], 'confidence': round(result['score'], 3)}
    chunks = split_text_into_chunks(context, max_chunk_size=800)
    best_answer, best_confidence = None, 0
    for chunk in chunks:
        result = qa_pipeline(question=question, context=chunk)
        if result['score'] > best_confidence:
            best_confidence = result['score']
            best_answer = result['answer']
    return {'answer': best_answer, 'confidence': round(best_confidence, 3)}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize_api():
    data = request.get_json()
    text = data.get('text', '')
    max_length = int(data.get('max_length', 150))
    min_length = int(data.get('min_length', 30))
    result = summarize_text(text, max_length, min_length)
    return jsonify({'summary': result})

@app.route('/qa', methods=['POST'])
def qa_api():
    data = request.get_json()
    question = data.get('question', '')
    context = data.get('context', '')
    result = answer_question(question, context)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
