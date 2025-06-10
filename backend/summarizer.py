import pdfplumber
from transformers import pipeline
from dotenv import load_dotenv
import os

load_dotenv()

def extract_text(pdf_path):
    """Extract text from PDF using pdfplumber"""
    with pdfplumber.open(pdf_path) as pdf:
        return " ".join(page.extract_text() for page in pdf.pages)

def summarize(text, model="t5-small"):
    """Summarize text using T5-small model"""
    summarizer = pipeline("summarization", model=model)
    
    # T5 works better with "summarize: " prefix
    input_text = "summarize: " + text[:1024]  # Truncate to avoid OOM errors
    
    summary = summarizer(
        input_text,
        max_length=150,
        min_length=30,
        do_sample=False
    )
    return summary[0]['summary_text']