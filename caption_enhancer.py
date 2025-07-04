import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def enhance_caption(raw_caption):
    prompt = f"Make this image caption more descriptive and engaging for social media: '{raw_caption}'"
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
        max_tokens=100
    )
    return response['choices'][0]['message']['content']
