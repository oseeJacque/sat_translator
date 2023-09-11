import pyttsx3
import streamlit as st
import os
from gtts import gTTS
from langdetect import detect
from pydub import AudioSegment

st.set_page_config(
page_title="sat_translator",
    page_icon="🗣",
    layout="wide"
)
genders = ['male', 'female']
error = False
st.title("Translate Text to Audio")
text = st.text_area("Write your text here")

#selected_language = st.selectbox("Select language", options=language, format_func=lambda x: x[1])
selected_gender = st.selectbox("Select the Gender", options=genders)

if st.button("Generate Audio"):
    if text:
        if len(text.split()) >= 10:
            error = False
            try:
                langue_detectee = detect(text)
                if selected_gender == 'female':
                    # Générate audio with TTS
                    st.write(langue_detectee)
                    tts = gTTS(text, lang=langue_detectee)

                    # Save audio in tempory memory
                    audio_filename = "output_audio.mp3"
                    tts.save(audio_filename)

                    # Display audio
                    st.audio(audio_filename)

                    # Delete Audio from tempory memory
                    os.remove(audio_filename)
                else:
                    engine = pyttsx3.init()
                    # Définir la voix (vous pouvez sélectionner parmi les voix disponibles sur votre système)
                    engine.setProperty('rates', 200)
                    engine.setProperty('volume', 1)  # Utilisez la première voix disponible

                    # Générer l'audio au format .wav
                    engine.save_to_file(text, 'output_audio.wav')
                    engine.runAndWait()

                    # Charger l'audio au format .wav avec pydub
                    audio = AudioSegment.from_wav('output_audio.wav')

                    # Afficher l'audio dans Streamlit
                    st.audio('output_audio.wav', format='audio/wav')
                    os.remove('output_audio.wav')
            except Exception as e:
                st.error(f"We have not detect the text language. Error : {e}")

        else:
            st.error("The text must be at least 15 words")
    else:
        st.error("The text must be at least 15 words")