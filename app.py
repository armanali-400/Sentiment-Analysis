import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline
import torch

# Load the trained model and tokenizer
MODEL_PATH = "sentiment_model"  # Make sure this folder exists
device = "cuda" if torch.cuda.is_available() else "cpu"

model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH).to(device)
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
classifier = pipeline("text-classification", model=model, tokenizer=tokenizer, device=0 if torch.cuda.is_available() else -1)

# Streamlit UI
st.title("💬 Sentiment Analysis with DistilBERT")
st.write("Enter a movie review below, and the model will classify it as **Positive** or **Negative**.")

user_input = st.text_area("Enter a review:", "")

if st.button("Analyze Sentiment"):
    if user_input:
        with st.spinner("Analyzing..."):
            result = classifier(user_input)[0]
            sentiment = result["label"]
            confidence = round(result["score"] * 100, 2)
            st.success(f"**Sentiment:** {sentiment} (Confidence: {confidence}%)")
    else:
        st.warning("Please enter some text for analysis.")
