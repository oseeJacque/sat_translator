import streamlit as st

import speech_recognition as sr
from pydub import AudioSegment

from src.utils.utils import language

st.set_page_config(
page_title="Multipage App",
    page_icon="👋",
layout="wide"
)

st.title("Translate Audio to Text")
audio_file = st.file_uploader("Upload Audio", type=["wav", "mp3", "m4a"])
selected_language = st.selectbox("Sélectionnez une langue", options=language, format_func=lambda x: x[1])
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
            text = recognizer.recognize_google(audio, language=selected_language[0])

        # Affichage du texte extrait
        st.write("Texte extrait de l'audio :")
        st.write(text)
    else:
        st.error("Veuillez télécharger un fichier audio.")