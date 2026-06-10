import streamlit as st
from PIL import Image
import ollama
from transformers import VisionEncoderDecoderModel
from transformers import ViTImageProcessor
from transformers import AutoTokenizer

# =========================
# PAGE CONFIG
# =========================

st.set_page_config(
    page_title="Image Caption Generator",
    page_icon="🖼️",
    layout="wide"
)

st.markdown("""
<style>

.main{
    background-color:#0E1117;
}

h1{
    color:#4CAF50;
    text-align:center;
}

.subtitle{
    color:gray;
    text-align:center;
    margin-bottom:30px;
}

.caption-box{
    background-color:#1E1E1E;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #4CAF50;
    margin-top:20px;
}

.stButton>button{
    background-color:#4CAF50;
    color:white;
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================

st.markdown("""
# 🖼️ Image Caption Generator

Upload an image and generate captions using AI.
""")

# =========================
# LOAD MODEL
# =========================

@st.cache_resource
def load_model():

    model = VisionEncoderDecoderModel.from_pretrained(
        "nlpconnect/vit-gpt2-image-captioning"
    )

    processor = ViTImageProcessor.from_pretrained(
        "nlpconnect/vit-gpt2-image-captioning"
    )

    tokenizer = AutoTokenizer.from_pretrained(
        "nlpconnect/vit-gpt2-image-captioning"
    )

    return model, processor, tokenizer


model, processor, tokenizer = load_model()

# =========================
# FILE UPLOAD
# =========================

caption_style = st.selectbox(
    "Caption Style",
    [
        "Normal",
        "Detailed",
        "Funny",
        "Instagram",
        "Story"
    ]
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

# =========================
# MAIN APP
# =========================

if uploaded_file:

    image = Image.open(uploaded_file)

    st.image(
        image,
        caption="Uploaded Image",
        use_container_width=True
    )

    with st.spinner(
        "Generating caption..."
    ):

        pixel_values = processor(
            images=image,
            return_tensors="pt"
        ).pixel_values

        output_ids = model.generate(
            pixel_values,
            max_length=30
        )

        caption = tokenizer.decode(
            output_ids[0],
            skip_special_tokens=True
        )
        final_caption = caption

        if caption_style != "Normal":

            prompt = f"""
        Image caption:

        {caption}

        """

            if caption_style == "Detailed":

                prompt += """
        Expand the caption.

        Describe objects, surroundings and colors.

        Respond directly with 2-3 sentences.
        """

            elif caption_style == "Funny":

                prompt += """
        Create one funny caption.

        Respond with only one sentence.

        Example:

        "When you promised to fetch the ball but got distracted by life."
        """

            elif caption_style == "Instagram":

                prompt += """
        Convert this into an Instagram caption.

        Include 2-3 emojis.

        Keep it under two sentences.

        Respond with only the caption.

        Example:

        "Living my best life in the sunshine 🐶☀️❤️"
        """

            elif caption_style == "Story":

                prompt += """
        Write a short and imaginative story inspired by the image.

        Keep it under 100 words.

        Respond directly.
        """

            with st.spinner("🤖 Enhancing caption..."):

                response = ollama.chat(
                    model="qwen3:1.7b",
                    messages=[
                        {
                            "role": "user",
                            "content": prompt
                        }
                    ],
                    think=False,
                    options={
                        "temperature": 0.3,
                        "num_predict": 200
                    }
                )

                final_caption = response["message"]["content"]
    st.success(
        "Caption Generated"
    )

    st.markdown(
    f"""
    <div class="caption-box">

    <h2>📷 Generated Caption</h2>

    {final_caption}

    </div>
    """,
    unsafe_allow_html=True
    )