# News Summarization & Hindi TTS Application

##  Overview  
This project extracts news articles related to a company, summarizes them, performs sentiment analysis, and generates a Hindi audio report.

 **Key Features:**  
 Web Scraping for latest news (BeautifulSoup)  
 Summarization using Transformers (Hugging Face)  
 Sentiment Analysis (Positive, Negative, Neutral)  
 Comparative Sentiment Insights  
 Hindi TTS Audio Output (gTTS)  
 API Support for analysis & querying
 API Support using Flask (`api.py`)  
 Web UI using Gradio (`app.py`) 

##  Project Setup, Model Details, API Development, API Usage, Assumptions & Deployment  
### **Project Setup**  
 **Clone the Repository**  
```bash
git clone https://github.com/guruprashanth2004/news-summarization-tts.git
cd news-summarization-tts
```
### **set up virtual environment**
```bash
python -m venv venv
venv\Scripts\activate
```
### **Install Dependencies**
```bash
pip install -r requirements.txt
```
### **Run the API**
```bash
python api.py
```
### **Run the Application**
```bash
python app.py
```
### **Model Details**  

#### **Summarization Model**    
- **Purpose:** Summarizes news articles into concise summaries.  
- **Library Used:** `transformers`
  
#### **Sentiment Analysis Model**  
- **Purpose:** Analyzes sentiment of news articles.  
- **Library Used:** `transformers`    

#### **Text-to-Speech (TTS) Model**  
- **Model:** `gTTS` (Google Text-to-Speech)  
- **Purpose:** Converts summarized sentiment analysis into Hindi speech.  
- **Library Used:** `gtts`  
- **Example Input:** `"Tesla की हालिया खबरें ज्यादातर सकारात्मक हैं।"`  
- **Example Output:** `output.mp3` (Hindi speech file)  

---

### **API Development (`api.py`)  
The backend API is built using **Flask** and provides two endpoints:  

#### **Analyze News (`/analyze`)**  
**Purpose:** Fetch news, summarize, analyze sentiment, and generate Hindi TTS.  
**Method:** `GET`  
**URL:**  
http://127.0.0.1:5000/analyze?company=Tesla
 **Response:**  
```json
{
    "articles": [
        {
            "title": "Tesla Stock Hits New Highs",
            "summary": "Tesla's stock price reached record levels...",
            "sentiment": "Positive"
        }
    ],
    "comparison": {
        "Sentiment Distribution": {"Positive": 1, "Negative": 0, "Neutral": 0}
    },
    "audio_file": "output.mp3"
}
```
#### **Query News by Sentiment (/query)**
 **Purpose:** Fetch articles based on sentiment filter.
 **Method:** GET
 **URL:**
http://127.0.0.1:5000/query?company=Tesla&sentiment=Positive
 **Response:**

``` json
{
    "articles": [
        {
            "title": "Tesla's Profits Rise",
            "summary": "Tesla reports record-breaking profits...",
            "sentiment": "Positive"
        }
    ]
}
```

#### **Third-Party APIs & Tools Used**

| API/Tool                     | Purpose                                      |
|------------------------------|----------------------------------------------|
| **Bing News Scraping**       | Extracts latest news articles               |
| **Hugging Face Transformers** | Summarization & Sentiment Analysis         |
| **Google Text-to-Speech (gTTS)** | Converts sentiment report to Hindi speech |

### **Assumptions & Limitations**
 #### **Assumptions**
- The news articles contain relevant information about the company.
- Sentiment analysis is reasonably accurate, but may misinterpret sarcasm.
- The Hindi TTS model correctly pronounces the text, but may have intonation issues.
 #### **Limitations**
- Web Scraping Issues:
- Some websites block bots (may require rotating proxies).
- Bing News doesn’t always provide full article content.
- Sentiment Model Limitations:
- Works well for English news, but doesn’t analyze Hindi news.
- #### *works better when deployed in vs code than in hugging face*

#### **Deployment**
This application is deployed on Hugging Face Spaces.

🔗 Live Demo: https://huggingface.co/spaces/guru14102004/news-summarization-tts

