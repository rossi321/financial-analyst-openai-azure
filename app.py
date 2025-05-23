import streamlit as st
from openai import AzureOpenAI
import os

# Set your Azure OpenAI config
AZURE_OPENAI_KEY = "your-key-here"
AZURE_OPENAI_ENDPOINT = "https://your-resource-name.openai.azure.com/"
AZURE_OPENAI_DEPLOYMENT = "your-deployment-name"

# Setup OpenAI client
client = AzureOpenAI(
    api_key=AZURE_OPENAI_KEY,
    api_version="2023-05-15",
    azure_endpoint=AZURE_OPENAI_ENDPOINT
)

# UI
st.title("💼 Financial Analyst Assistant")
st.write("Upload an earnings call transcript and ask a question.")

uploaded_file = st.file_uploader("📄 Upload a .txt document", type="txt")
question = st.text_input("💬 What would you like to ask?")

if uploaded_file and question:
    document = uploaded_file.read().decode("utf-8")
    prompt = f"""You are a financial analyst assistant. Use the following document to answer the question.

Document:
{document}

Question: {question}
Answer:"""

    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model=AZURE_OPENAI_DEPLOYMENT,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=300
        )
        answer = response.choices[0].message.content
        st.markdown("### 🧠 Answer")
        st.success(answer)