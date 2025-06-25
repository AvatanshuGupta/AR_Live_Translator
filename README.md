# AR Translator – Real-Time English to Hindi Translation

A real-time Augmented Reality (AR) application that detects English text from a live webcam feed using EasyOCR, translates it to Hindi using Google Translate, and overlays the translated Hindi text directly on the video feed. This project is ideal for language learners, travelers, or accessibility tools.

---

## Features

- Real-time English text detection using EasyOCR
- Translates detected text from English to Hindi using Google Translate
- Overlays Hindi text on the video feed using PIL with Devanagari font support
- CUDA GPU support for fast OCR (if available)
- Customizable OCR frequency and display duration

---

## Requirements

Make sure you have the following installed before running the project:

### 1. Python Version

- Python 3.7 or higher (Python 3.7 to 3.11 recommended for best compatibility)

### 2. Operating System

- Windows, macOS, or Linux
- For GPU acceleration (optional):
  - NVIDIA GPU with CUDA 11.1 or higher
  - CUDA Toolkit and cuDNN installed correctly

### 3. Python Packages

Install all dependencies using pip:

```bash
pip install easyocr googletrans==4.0.0-rc1 opencv-python numpy pillow

