import streamlit as st
from PIL import Image
from caption_generator import generate_caption
from caption_enhancer import enhance_caption

st.set_page_config(page_title="🖼️ Image-to-Caption Generator")
st.title("🖼️ Image-to-Caption Generator")
st.write("Upload an image and get an automatic natural language caption.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)

    with st.spinner("Generating caption..."):
        raw_caption = generate_caption(image)
        st.markdown(f"### 🧾 Raw Caption:\n{raw_caption}")

        if st.checkbox("Enhance caption for social media"):
            enhanced = enhance_caption(raw_caption)
            st.markdown(f"### ✨ Enhanced Caption:\n{enhanced}")