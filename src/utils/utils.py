
from pydub import AudioSegment
import speech_recognition as sr

language = [
    ('en', 'Anglais'),
    ('es', 'Espagnol'),
    ('fr', 'Français'),
    ('de', 'Allemand'),
    ('it', 'Italien'),
    ('pt', 'Portugais'),
    ('nl', 'Néerlandais'),
    ('ru', 'Russe'),
    ('zh-CN', 'Chinois simplifié'),
    ('zh-TW', 'Chinois traditionnel'),
    ('ja', 'Japonais'),
    ('ko', 'Coréen'),
    ('ar', 'Arabe'),
    ('he', 'Hébreu'),
    ('tr', 'Turc'),
    ('el', 'Grec'),
    ('hi', 'Hindi'),
    ('bn', 'Bengali'),
    ('te', 'Télougou'),
    ('ta', 'Tamoul'),
    ('ur', 'Urdu'),
    ('th', 'Thaï'),
    ('id', 'Indonésien'),
    ('ms', 'Malais'),
    ('vi', 'Vietnamien'),
    ('fil', 'Philippin'),
    ('pl', 'Polonais'),
    ('sv', 'Suédois'),
    ('no', 'Norvégien'),
    ('da', 'Danois'),
    ('fi', 'Finnois'),
    ('hu', 'Hongrois'),
    ('cs', 'Tchèque'),
    ('sk', 'Slovaque'),
    ('ro', 'Roumain'),
    ('bg', 'Bulgare'),
    ('ka', 'Géorgien'),
    ('sw', 'Swahili'),
    ('tk', 'Turkmène'),
    ('kk', 'Kazakh'),
]


def audio_to_text(audio_bytes,language):
    # Convertir les données audio en un fichier temporaire au format .wav
    with open("temp_audio.wav", "wb") as audio_file:
        audio_file.write(audio_bytes)

    # Charger le fichier audio au format .wav
    audio = AudioSegment.from_wav("temp_audio.wav")

    # Initialiser le reconnaisseur vocal
    recognizer = sr.Recognizer()

    # Reconnaître le texte à partir de l'audio
    try:
        with sr.AudioFile("temp_audio.wav") as source:
            audio_data = recognizer.record(source)  # Enregistrer l'audio
            text = recognizer.recognize_google(audio_data,language=language)  # Reconnaître le texte en utilisant Google Speech Recognition
            return text
    except sr.UnknownValueError:
        return "Impossible de reconnaître l'audio."
    except sr.RequestError as e:
        return f"Erreur lors de la demande au service Google Speech Recognition : {e}"