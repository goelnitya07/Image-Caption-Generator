# 🖼️ AI Image Caption Generator

An intelligent Image Caption Generator built with **Streamlit**, **Hugging Face Transformers**, and **Ollama**.

Upload any image and generate captions in multiple styles using computer vision and local LLMs.

---

## ✨ Features

- 📷 Upload JPG, JPEG, and PNG images
- 🤖 Automatic image caption generation using ViT-GPT2
- 🎭 Multiple caption styles:
  - Normal
  - Detailed
  - Funny
  - Instagram
  - Story
  - Professional
- 🧠 AI-enhanced captions powered by Qwen 3 via Ollama
- 🌙 Dark-themed Streamlit interface
- ⚡ Fast local inference
- 🔒 Fully offline AI pipeline

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Hugging Face Transformers
- ViT-GPT2 Image Captioning Model
- Ollama
- Qwen3 1.7B
- Pillow

---

## 📂 Project Structure

```
Image-Caption-Generator/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
└── sample_images/
```

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/Image-Caption-Generator.git

cd Image-Caption-Generator
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Activate:

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Install Ollama

Download Ollama:

https://ollama.com/download

Pull Qwen3:

```bash
ollama pull qwen3:1.7b
```

---

## Run the Application

```bash
streamlit run app.py
```

---

## Example Caption Styles

### Normal

> A dog laying on grass with a ball in its mouth.

### Funny

> When you promised to fetch the ball but got distracted by life.

### Instagram

> Living my best life in the sunshine 🐶☀️❤️

### Story

> A playful dog spent the afternoon enjoying the warm sunshine, guarding its favorite ball like a treasured prize.

---

## Future Improvements

- 📜 Caption history
- 📥 Download captions
- 📊 Caption statistics
- 🔍 OCR text extraction
- 🎯 Object detection using YOLO
- 🌍 Multilingual captions

---

## Built With

- Streamlit
- Hugging Face Transformers
- Ollama
- Qwen3 1.7B

---

## Author

**Nitya Goel**

GitHub:
https://github.com/goelnitya07

---

### ⭐ If you found this project useful, consider giving it a star!