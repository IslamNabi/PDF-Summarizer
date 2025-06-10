import streamlit as st
import requests

st.title("📄 AI PDF Summarizer")
uploaded_file = st.file_uploader("Upload PDF", type="pdf")

if uploaded_file:
    if st.button("Summarize"):
        try:
            files = {"file": uploaded_file}
            response = requests.post(
                "http://localhost:5000/summarize", 
                files=files
            )
            
            if response.status_code == 200:
                st.subheader("Summary")
                st.write(response.json()["summary"])
            else:
                st.error(f"Backend error: {response.text}")
                
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to connect to backend. Is Flask running? Error: {e}")