#importing modules
import requests
from bs4 import BeautifulSoup
from transformers import pipeline
from gtts import gTTS
import pandas as pd

# News_Scraping function
def get_news_articles(company_name):
    search_url = f"https://www.bing.com/news/search?q={company_name}"  #using bing for news scraping
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.find_all("a", {"class": "title"}):
        title = item.text.strip()
        link = item["href"]
        articles.append({"title": title, "link": link})

        if len(articles) >= 10:
            break

    return articles

# Summarization function
summarizer = pipeline("summarization")

def summarize_text(text):
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]["summary_text"]

# Sentiment Analysis function
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)
    return result[0]["label"]

# Comparative Sentiment function
def compare_sentiments(articles):
    df = pd.DataFrame(articles)
    sentiment_counts = df["sentiment"].value_counts().to_dict()

    most_positive = df[df["sentiment"] == "Positive"].head(1).to_dict(orient="records")
    most_negative = df[df["sentiment"] == "Negative"].head(1).to_dict(orient="records")

    return {
        "Sentiment Distribution": sentiment_counts,
        "Most Positive Article": most_positive,
        "Most Negative Article": most_negative
    }

# Text to speech in hindi
def text_to_speech_hindi(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="hi", slow=False)
    tts.save(filename)
    return filename
