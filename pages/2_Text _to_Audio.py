import streamlit as st
import os
from gtts import gTTS

from src.utils.utils import language

st.set_page_config(
page_title="Multipage App",
    page_icon="👋",
    layout="wide"
)
genders = ['male', 'female']
st.title("Translate Text to Audio")
text = st.text_area("Écrivez votre texte ici")
selected_language = st.selectbox("Select language", options=language, format_func=lambda x: x[1])
selected_gender = st.selectbox("Select the sex", options=genders)

if st.button("Generate Audio"):
    if text:
        # Générate audio with TTS
        tts = gTTS(text, lang=selected_language[0])

        # Save audio in tempory memory
        audio_filename = "output_audio.mp3"
        tts.save(audio_filename)

        # Display audio
        st.audio(audio_filename)

        # Delete Audio from tempory memory
        os.remove(audio_filename)

    else:
        st.error("Veuillez écrire le texte à traduire en audio.")
