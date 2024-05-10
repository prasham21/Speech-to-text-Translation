import streamlit as st

from constants import (
    STATUS_ENDPOINT,
    LOCAL_FILE__TRANSCRIPTION_ENDPOINT,
    YOUTUBE_TRANSCRIPTION_ENDPOINT,
    LIVE_TRANSCRIPTION_WEBSOCKET_ENDPOINT,
    WHISPER_SAMPLING_RATE,
)
from utils import (
    handle_local_file_transcription,
    handle_youtube_transcription,
    handle_live_transcription,
)

# Set page configuration
st.set_page_config(
    page_title="Transcription Tool",
    page_icon=":microphone:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sidebar styles
st.markdown(
    """
    <style>
        .sidebar .sidebar-content {
            background-color: #2e3f4f;
            color: #ffffff;
        }
        .sidebar .sidebar-content .block-container a {
            color: #ffffff;
        }
    </style>
""",
    unsafe_allow_html=True,
)

# Main content styles
st.markdown(
    """
    <style>
        .css-1v1pxco {
            color: #ffffff;
        }
        .css-hi6a2p {
            background-color: #465a6b;
            border-radius: 10px;
            padding: 20px;
            box-shadow: 0px 0px 10px 0px rgba(0,0,0,0.1);
        }
        .stButton>button {
            background-color: #007bff;
            color: #ffffff;
            border-radius: 5px;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stTextInput>div>div>input {
            background-color: #ffffff;
            color: #333333;
            border-radius: 5px;
        }
        .stTextInput>div>div>input:focus {
            border-color: #007bff;
        }
    </style>
""",
    unsafe_allow_html=True,
)

if __name__ == "__main__":
    # Title of the application
    st.title("Advanced Transcription Tool")

    st.markdown(
        "Welcome to the Advanced Transcription Tool! This tool converts speech from audio files, YouTube videos, or live input into text. Select a mode and start transcribing!"
    )

    st.sidebar.markdown(
        """
        ## How to Use this Tool:
        Follow these steps to get your transcription:

        - **Select a mode of operation:** Choose whether to upload an audio file, enter a YouTube URL, or start live transcription.
        - **Upload or Input:** Based on the selected mode, either upload an audio file, enter a YouTube URL, or simply start speaking when prompted.
        - **Review:** Wait for the transcription to complete and then review your transcribed text.
        """
    )

    # Sidebar for mode selection
    transcription_mode = st.sidebar.radio(
        "Choose a mode of operation:",
        ("Transcribe Local File", "Transcribe from YouTube URL", "Transcribe Live"),
    )

    # Make the transition based on transcription mode selected by the user
    if transcription_mode == "Transcribe Local File":
        # Load the audio file from the local file manager
        uploaded_file = st.file_uploader("Choose a file", type=["wav"])
        transcribed_file = None

        # Define the endpoint of your FastAPI service
        fastapi_endpoint = LOCAL_FILE__TRANSCRIPTION_ENDPOINT
        status_endpoint = STATUS_ENDPOINT  # Endpoint to check the status

        # If the file is loaded and transcribe button is pressed, process the audio
        if uploaded_file is not None:
            if st.button("Transcribe Audio"):
                handle_local_file_transcription(
                    uploaded_file, fastapi_endpoint, status_endpoint
                )

    if transcription_mode == "Transcribe from YouTube URL":
        # Input for YouTube URL
        youtube_url = st.text_input("Enter YouTube Video URL")
        # Define the endpoint of your FastAPI service
        fastapi_endpoint_youtube = YOUTUBE_TRANSCRIPTION_ENDPOINT
        status_endpoint = STATUS_ENDPOINT

        # Handling the transcription request
        if youtube_url:
            if st.button("Transcribe Video"):
                handle_youtube_transcription(
                    youtube_url, fastapi_endpoint_youtube, status_endpoint
                )

    if transcription_mode == "Transcribe Live":
        # Initialize the session state for recording status
        st.session_state["stop_recording"] = False

        # Define the websocket url
        websocket_url = LIVE_TRANSCRIPTION_WEBSOCKET_ENDPOINT

        # Define the microphone input sampling rate same as whisper model
        sampling_rate = WHISPER_SAMPLING_RATE

        if st.button("Transcribe Live"):
            handle_live_transcription(sampling_rate, websocket_url)

        else:
            # If there is a transcription recorded display it
            if "live_transcription" in st.session_state.keys():
                # Create a container for text area
                transcription_display = st.empty()

                st.info(
                    "You can edit the transcription before downloading by editing the textbox and pressing Ctrl+Enter"
                )

                st.session_state[
                    "live_transcription"
                ] = transcription_display.text_area(
                    "Transcription",
                    value=st.session_state["live_transcription"],
                    height=300,
                )

                # Download button for the transcription
                st.download_button(
                    label="Download Transcription",
                    data=st.session_state["live_transcription"],
                    file_name="live_transcription.txt",
                    mime="text/plain",
                )

                # Reset the session state
                if st.button("Reset Transcription"):
                    st.session_state["live_transcription"] = ""
