import os

HOST = os.getenv("HOST", "localhost")
# Constants for transcription
STATUS_ENDPOINT = f"http://{HOST}:8000/status"

LOCAL_FILE__TRANSCRIPTION_ENDPOINT = f"http://{HOST}:8000/transcribe-local"
YOUTUBE_TRANSCRIPTION_ENDPOINT = f"http://{HOST}:8000/transcribe-youtube"
LIVE_TRANSCRIPTION_WEBSOCKET_ENDPOINT = f"ws://{HOST}:8000/ws"

WHISPER_SAMPLING_RATE = 16000
