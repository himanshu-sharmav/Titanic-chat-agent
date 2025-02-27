import streamlit as st
import requests
import base64
from PIL import Image
import io

# FastAPI backend URL
BACKEND_URL = "http://127.0.0.1:8000"

st.title("🚢 Titanic Dataset Chatbot")

# User Input
query = st.text_input("Ask a question about the Titanic dataset")

if st.button("Submit"):
    if query:
        with st.spinner("Thinking..."):
            # Fetch text response
            response = requests.get(f"{BACKEND_URL}/query/", params={"question": query}).json()
            st.write(response["response"])

            # Fetch visualization if applicable
            image_response = requests.get(f"{BACKEND_URL}/visualize/", params={"query": query}).json()
            if "image" in image_response:
                image_data = base64.b64decode(image_response["image"])
                image = Image.open(io.BytesIO(image_data))
                st.image(image)
            elif "error" in image_response:
                st.warning(image_response["error"])
    else:
        st.warning("Please enter a question.")
