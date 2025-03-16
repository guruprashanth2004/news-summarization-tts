#importing modules
from flask import Flask, request, jsonify
from utils import get_news_articles, summarize_text, analyze_sentiment, compare_sentiments, text_to_speech_hindi

app = Flask(__name__)

# routing by company
@app.route("/analyze", methods=["GET"])
def analyze():
    company_name = request.args.get("company")
    if not company_name:
        return jsonify({"error": "Company name is required"}), 400

    articles = get_news_articles(company_name)
    
    for article in articles:
        article["summary"] = summarize_text(article["title"])
        article["sentiment"] = analyze_sentiment(article["summary"])

    comparison = compare_sentiments(articles)
    
    hindi_summary = f"{company_name} की हालिया खबरें ज्यादातर {comparison['Sentiment Distribution']} हैं।"
    tts_file = text_to_speech_hindi(hindi_summary, "output.mp3")

    return jsonify({"articles": articles, "comparison": comparison, "audio_file": tts_file})

# API: Query News by Sentiment
@app.route("/query", methods=["GET"])
def query_news():
    company_name = request.args.get("company")
    filter_sentiment = request.args.get("sentiment")

    articles = get_news_articles(company_name)
    for article in articles:
        article["summary"] = summarize_text(article["title"])
        article["sentiment"] = analyze_sentiment(article["summary"])

    if filter_sentiment and filter_sentiment != "All":
        articles = [article for article in articles if article["sentiment"].lower() == filter_sentiment.lower()]

    return jsonify({"articles": articles})

if __name__ == "__main__":
    app.run(debug=True)
