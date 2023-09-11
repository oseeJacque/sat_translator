import streamlit as st

import speech_recognition as sr
from audio_recorder_streamlit import audio_recorder
from pydub import AudioSegment

from src.utils.utils import language, audio_to_text

st.set_page_config(
page_title="sat_translator",
    page_icon="🗣",
layout="wide"
)
text = ""
st.title("Translate Audio to Text")
col1, col2, col3 = st.columns([3, 1, 3])

#Upload audio
with col1:
    audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])

#or
with col2:
    st.write("Or")

#Audio  recording
with col3:
    #wav_audio_data = st_audiorec()
    audio_bytes = audio_recorder()
    st.audio(audio_bytes, format="audio/wav")

#Select transcription language for audio
selected_language = st.selectbox("Sélectionnez une langue", options=language, format_func=lambda x: x[1])

#Transcribe button and contrôle
if st.button("Transcribe Audio"):
    if audio_file is not None:

        # Convert audio to wav format
        audio_data = AudioSegment.from_file(audio_file)
        if audio_file.type != "wav":
            audio_file = audio_file.name.replace(audio_file.type, "wav")
            audio_data.export(audio_file, format="wav")

        # Audio to text
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
            try:
                text = recognizer.recognize_google(audio, language=selected_language[0])
                st.success("traduction succes!")
            except sr.UnknownValueError:
                st.error("Please select good language for audio!")
            except sr.RequestError as e:
                st.error(f"Something is wrong !!! : {e}")

    elif audio_bytes:

        try:
            text = audio_to_text(audio_bytes, language=selected_language[0])
        except sr.UnknownValueError:
            st.error("Please choose a language consistent with the audio")
        except sr.RequestError as e:
            st.error(f"Something is wrong: {e}")
    else:
        st.error("Dowload audio or speak with your microphone")

# Display text
st.write("Text:")
st.write(f'<div style="background-color: black; color: white; padding: 20px; white-space: pre-line; border-radius: 10px;">{text}</div>', unsafe_allow_html=True)