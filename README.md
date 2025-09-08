# Text-Summarizer
## 📄 AI Text Summarizer

This project is a Streamlit + Flask web application that generates concise and readable summaries from large text inputs using state-of-the-art NLP models. It provides users with a simple interface to paste any text, process it through a backend summarization model, and receive an optimized summary along with readability insights.

## 🔹 Features

- **AI-Powered Summarization: Uses the facebook/bart-large-cnn transformer model to generate accurate summaries.**
- **Word Count Analysis: Displays the original text’s word count for reference.**
- **Readability Score: Calculates the Flesch Reading Ease score for the summary using textstat.**
- **History Tracking: Saves previous summaries in session history with expandable details.**
- **Interactive UI: Built with Streamlit, featuring a styled interface with background image, custom fonts, and button animations.**
- **Backend API: Powered by Flask, handling summarization requests and returning JSON responses.**

🔹 Tech Stack
- **Frontend: Streamlit (Python)**
- **Backend: Flask (Python)**
- **NLP Model: Hugging Face Transformers (facebook/bart-large-cnn)**
- **Libraries: torch, transformers, textstat, requests, streamlit**

🔹 How It Works
- **User pastes text into the Streamlit interface.**
- **The app sends the text to the Flask backend via a POST request.**
- **The backend runs the text through the summarization model.**
- **The summary, word count, and readability score are returned.**
- **Results are displayed in the UI, and a history of past summaries is maintained.**
