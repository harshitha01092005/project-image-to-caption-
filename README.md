# Image-to-Caption Generator

A Streamlit app that:
✅ Generates captions using BLIP  
✅ Enhances captions using GPT  

## How to run

```bash
# 1. Clone/download this repo
# 2. Navigate to folder in VS Code
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
pip install -r requirements.txt
export OPENAI_API_KEY="your_api_key"
streamlit run app.py
