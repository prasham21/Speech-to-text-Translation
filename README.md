# Transcriptor Project

## Overview

Transcriptor is an advanced transcription tool that leverages the OpenAI Whisper Tiny model to convert speech from audio files, YouTube videos, or live input into text. It features a user-friendly frontend built with Streamlit and a robust backend designed with FastAPI and WebSockets, providing real-time transcription capabilities with high accuracy.

## Features

- Transcribe audio from local files (.wav format).
- Transcribe content directly from YouTube URLs.
- Real-time transcription through live audio input.
- Simple and intuitive user interface.
- Option to download transcriptions as a text file.
- Generates live SRT files using Silero VAD and Whisper which can be used in the video.

## How It Works

1. **Select a Mode of Operation**: Choose whether to upload an audio file, enter a YouTube URL, or start live transcription.
2. **Upload or Input**: Depending on the selected mode, either upload an audio file, enter a YouTube URL, or begin speaking when prompted.
3. **Review**: Wait for the transcription to complete and then review your transcribed text.
4. **Download**: Get a copy of the transcribed text by downloading it directly from the interface.

## Installation

To set up the Transcriptor project locally, you need to create a virtual environment and load the requirements in the requirements.txt file in 
the main folder after navigating the project directory.
This project requires ffmpeg module for real time transcriptions. Please install this module if necessary

1. Clone the repository (ssh example):
   ```sh
   git clone git@github.com:jainal09/data-science-capstone-assignment.git

2. Navigate to the project directory:
   ```sh
   cd data-science-capstone-assignment

3. In order to run the backend ggo to the backend directory and start the FASTAPI server
   ```sh
   cd backend
   uvicorn app:app --host 0.0.0.0 --port 8000

4. After running the backend, you need to start the streamlit frontend in another terminal, go to the frontend folder and run the streamlit app
   ```sh
   cd frontend
   streamlit run app.py

## Usage
The frontend at: http://localhost:8501
The backend at: http://localhost:8000

### Docker

```sh
docker compose up -d
```
It starts both the frontend and the backend communicating with eacb other.

## License
MIT License

Copyright (c) 2024 Jainal Gosaliya, Adarsh Gupta, Faizan Shaikh

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
   


## Citations

1. **OpenAI Whisper Tiny Model**: The core of Transcriptor's transcription capabilities is built upon the OpenAI Whisper Tiny model, a state-of-the-art Automatic Speech Recognition (ASR) model capable of transcribing speech in 99 languages with high accuracy [0].

2. **Hugging Face Whisper Tiny**: The Whisper Tiny model is available on Hugging Face, a platform that hosts a wide range of models for various NLP tasks, including ASR. This model is designed for both English-only and multilingual applications, with parameters ranging from 38M for tiny models to 1.5B for large models [0].

3. **Whisper Release and Collection**: The Whisper model collection includes both English-only and multilingual checkpoints for ASR and Speech-to-Text (ST), showcasing the versatility and efficiency of the model in different language and application scenarios [0].

4. **NB-Whisper Small Model**: The Norwegian NB-Whisper Small model, developed by the National Library of Norway, is based on the work of OpenAI's Whisper. This model has been trained on a diverse dataset of 8 million samples, demonstrating the potential for fine-tuning and adaptation of the Whisper model for specific language and domain applications [3].

5. **Whisper's Code and Model Weights**: The code and model weights for Whisper are released under the MIT License, making it accessible for developers and researchers to build upon and integrate into their projects. This open-source approach facilitates the development of advanced transcription tools like Transcriptor [4].
