#importing modules
import gradio as gr
import requests

# Flask API url
API_URL_ANALYZE = "http://127.0.0.1:5000/analyze"
API_URL_QUERY = "http://127.0.0.1:5000/query"

# function to fetch and analyze news
def analyze_news(company_name):
    response = requests.get(API_URL_ANALYZE, params={"company": company_name})
    if response.status_code != 200:
        return "Error: Could not fetch data."

    result = response.json()
    return result["articles"], result["comparison"], result["audio_file"]

# function to query news based on sentiment
def query_news(company_name, sentiment):
    params = {"company": company_name}
    if sentiment != "All":
        params["sentiment"] = sentiment

    response = requests.get(API_URL_QUERY, params=params)
    if response.status_code != 200:
        return "Error fetching news."

    return response.json()["articles"]

# interface
with gr.Blocks() as demo:
    gr.Markdown("# News Summarization & Sentiment Analysis")
    
    with gr.Row():
        company_input = gr.Textbox(label="Enter Company Name")
        analyze_btn = gr.Button("Analyze")

    articles_output = gr.JSON(label="News Articles")
    comparison_output = gr.JSON(label="Sentiment Analysis Report")
    audio_output = gr.Audio(label="Hindi Audio Summary")

    analyze_btn.click(analyze_news, inputs=company_input, outputs=[articles_output, comparison_output, audio_output])

    # Query Section
    gr.Markdown("### Query News by Sentiment")
    sentiment_filter = gr.Dropdown(["All", "Positive", "Negative", "Neutral"], label="Filter Sentiment")
    query_btn = gr.Button("Search")

    query_output = gr.JSON(label="Filtered Articles")
    query_btn.click(query_news, inputs=[company_input, sentiment_filter], outputs=query_output)

demo.launch()
