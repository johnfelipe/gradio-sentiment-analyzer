#import libraries
#import imp
from transformers import pipeline
sentiment_analysis_pipeline = pipeline("sentiment-analysis")
import gradio as gr

#sentimet_analysis
def sentiment_analysis(text):
    label=sentiment_analysis_pipeline(text)[0]['label']
    value=str(round(sentiment_analysis_pipeline(text)[0]['score']*100,2))+"%"
    return label+"...."+value

#interface
interface=gr.Interface(sentiment_analysis,
                       gr.inputs.Textbox(lines=7,placeholder="Enter your text here..."),
                       outputs=["text"],title="Sentiment Analysis")
interface.launch(share=True)