function switchTab(tabName, event) {
    document.querySelectorAll('.tab').forEach(tab => tab.classList.remove('active'));
    document.querySelectorAll('.content-panel').forEach(panel => panel.classList.remove('active'));
    event.target.classList.add('active');
    document.getElementById(tabName).classList.add('active');
}

function summarizeText() {
    const text = document.getElementById('textInput').value.trim();
    const maxLength = parseInt(document.getElementById('maxLength').value);
    const minLength = parseInt(document.getElementById('minLength').value);

    if (!text) return showError('Please enter text.', 'summaryResult');

    showLoading('summaryResult', 'Generating summary...');
    fetch('/summarize', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text, max_length: maxLength, min_length: minLength })
    })
    .then(res => res.json())
    .then(data => showResult(data.summary, 'summaryResult'))
    .catch(err => showError('Error processing request.', 'summaryResult'));
}

function answerQuestion() {
    const context = document.getElementById('contextInput').value.trim();
    const question = document.getElementById('questionInput').value.trim();

    if (!context) return showError('Please enter context text.', 'qaResult');
    if (!question) return showError('Please enter a question.', 'qaResult');

    showLoading('qaResult', 'Finding answer...');
    fetch('/qa', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ context, question })
    })
    .then(res => res.json())
    .then(data => showAnswerResult(data, 'qaResult'))
    .catch(err => showError('Error processing request.', 'qaResult'));
}

function showError(message, resultId) {
    document.getElementById(resultId).innerHTML = `<div style="color:red">${message}</div>`;
}

function showLoading(resultId, message) {
    document.getElementById(resultId).innerHTML = `<div style="color:blue">${message}</div>`;
}

function showResult(text, resultId) {
    document.getElementById(resultId).innerHTML = `<div>${text}</div>`;
}

function showAnswerResult(result, resultId) {
    document.getElementById(resultId).innerHTML = `<div><b>Answer:</b> ${result.answer}</div>
    <div>Confidence: ${(result.confidence * 100).toFixed(1)}%</div>`;
}
