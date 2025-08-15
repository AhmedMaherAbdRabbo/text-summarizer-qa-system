# AI Text Analysis Suite

> **A powerful AI-driven web application for intelligent text summarization and question answering using state-of-the-art transformer models.**

## 🎯 Project Overview

This project provides a comprehensive **AI Text Analysis Suite** featuring advanced natural language processing capabilities. The system combines **BART-Large-CNN** for text summarization and **RoBERTa-Base-SQuAD2** for question answering, all deployed through a modern, interactive web interface built with Flask.

### ✨ Key Features

- **Intelligent Text Summarization**: BART-Large-CNN model for high-quality summaries
- **Advanced Question Answering**: RoBERTa-Base-SQuAD2 for precise answer extraction
- **Smart Text Processing**: Automatic text chunking for long documents
- **Interactive Web Interface**: Modern, responsive UI with real-time processing
- **Confidence Scoring**: Answer confidence levels for reliability assessment
- **Customizable Parameters**: Adjustable summary length and processing settings
- **Production Ready**: Complete deployment solution with optimized models

## 📊 Model Performance

### Text Summarization (BART-Large-CNN)
- **Model**: Facebook's BART-Large fine-tuned on CNN/DailyMail
- **Capabilities**: Extractive and abstractive summarization
- **Max Input**: Up to 1024 tokens per chunk
- **Features**: Automatic text chunking for long documents

### Question Answering (RoBERTa-Base-SQuAD2)
- **Model**: RoBERTa-Base fine-tuned on SQuAD 2.0
- **Accuracy**: State-of-the-art performance on SQuAD benchmarks
- **Features**: Confidence scoring and "no answer" detection
- **Context Processing**: Smart chunking for long context texts

## 📁 Project Structure

```
text-summarizer-qa/
│
├── 📁 notebook/                     # Model Development
│   └── Text_Summarizer_Question_Answering.ipynb
│
├── 📁 templates/                    # HTML Templates
│   └── index.html                  # Main web interface
│
├── 📁 static/                      # Frontend Assets
│   ├── 📁 css/
│   │   └── styles.css              # Modern CSS styling
│   └── 📁 js/
│       └── script.js               # Interactive JavaScript
│
├── 📄 app.py                       # Flask application server
├── 📄 requirements.txt             # Python dependencies
├── 📄 README.md                    # Project documentation
└── 📄 LICENSE                      # MIT License
```

## 🔧 Core Features

### 📄 Text Summarization
- **Smart Chunking**: Automatically splits long texts into processable chunks
- **Customizable Length**: Adjustable min/max summary lengths
- **Merge Summaries**: Combines multiple chunk summaries intelligently
- **Quality Control**: Minimum text length validation

### ❓ Question Answering
- **Context Processing**: Handles long documents through intelligent chunking
- **Confidence Scoring**: Provides reliability scores for answers
- **Best Answer Selection**: Chooses highest confidence answer across chunks
- **No Answer Detection**: Identifies when questions cannot be answered


## 📈 Performance Optimization

### Model Loading
- **Lazy Loading**: Models loaded on application startup
- **Memory Management**: Efficient tensor operations
- **Framework Selection**: PyTorch backend for optimal performance

### Processing Optimization
- **Chunk Size Optimization**: Balanced for quality and speed
- **Batch Processing**: Efficient handling of multiple chunks
- **Error Handling**: Robust error recovery and user feedback


## 📋 Dependencies

### Core Libraries
- **Flask**: Web framework for Python
- **transformers**: Hugging Face transformers library
- **torch**: PyTorch deep learning framework
- **re**: Regular expressions for text processing

### Model Requirements
- **facebook/bart-large-cnn**: Text summarization model (~1.6GB)
- **deepset/roberta-base-squad2**: Question answering model (~500MB)


## 🤝 Contributing

Feel free to suggest improvements, fix bugs, or add new features.  
Thanks for your support.

## 📞 Contact

**Ahmed Maher Abd Rabbo**
- 💼 [LinkedIn](https://www.linkedin.com/in/ahmed-maherr/)
- 📊 [Kaggle](https://kaggle.com/ahmedmaherabdrabbo)
- 📧 Email: ahmedbnmaher1@gmail.com
- 💻 [GitHub](https://github.com/AhmedMaherAbdRabbo)

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
