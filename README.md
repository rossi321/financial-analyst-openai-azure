# Azure OpenAI Financial Analyst Assistant

This project demonstrates how to use Azure OpenAI and Streamlit to build a lightweight financial analyst assistant. The app enables users to upload earnings call transcripts and query them using a GPT-powered natural language interface.

## 🚀 Features
- Upload `.txt` files (e.g., earnings call transcripts)
- Ask questions and get contextual answers using Azure-hosted GPT-35 Turbo
- Fast and simple Streamlit UI
- Includes architecture diagram and blog write-up
- Future integrations: Blob Storage, Cognitive Search, Power BI

## 🛠 Tech Stack
- Azure OpenAI Service (GPT-35 Turbo)
- Streamlit (frontend)
- Python
- Optional: Azure Blob Storage, Azure Cognitive Search, Cosmos DB

## 📁 Project Structure
```
.
├── app.py
├── requirements.txt
├── q2_earnings_call.txt
├── architecture/
│   ├── Simple_Azure_OpenAI_Architecture.png
│   └── Earnings_Call_Insight_Diagram.png
├── blog/
│   └── Azure_OpenAI_Blog_Post.docx
├── slides/
│   └── Azure_OpenAI_Diagram_Slide.pptx
```

## 📄 Blog Post
Read the full story: *Coming Soon on Medium*

## 📥 How to Run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## 🧠 Author
Built by [Your Name] — connect on [LinkedIn](#)

## 🧪 Notebooks
- [Azure OpenAI Financial Demo](notebooks/Azure_OpenAI_Financial_Demo.ipynb) – Step-by-step Jupyter notebook version of the assistant logic