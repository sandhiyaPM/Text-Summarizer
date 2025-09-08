from flask import Flask, request, jsonify
from transformers import pipeline
import torch
import textstat 

app = Flask(__name__)

# Load summarization model
device = 0 if torch.cuda.is_available() else -1
print(f"Device set to use {'GPU' if device == 0 else 'CPU'}")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", device=device)

@app.route("/summarize", methods=["POST"])
def summarize():
    data = request.get_json()
    text = data.get("text", "")

    if not text.strip():
        return jsonify({"error": "No text provided"}), 400

    # Generate summary
    summary_output = summarizer(
        text,
        max_length=150,
        min_length=40,
        do_sample=False
    )
    summary_text = summary_output[0]["summary_text"]

    # Word count of original text
    word_count = len(text.split())

    # ✅ Readability score (Flesch Reading Ease)
    readability_score = textstat.flesch_reading_ease(summary_text)

    return jsonify({
        "summary": summary_text,
        "word_count": word_count,
        "readability_score": readability_score   # ✅ added
    })

if __name__ == "__main__":
    app.run(debug=True)

