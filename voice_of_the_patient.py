#setup audio recorder (ffmpeg && portaudio)
#brew install ffmeg , brew install portaudio

import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20 , phrase_time_limit=None):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            logging.info("Adjusting for ambient noise...")
            recognizer.adjust_for_ambient_noise(source, duration=1)
            logging.info("Start Speaking Now...")

            #record the audio
            audio_data = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
            logging.info("Recording finished.")

            #convert the audio to mp3 format
            wav_data = audio_data.get_wav_data()
            audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
            audio_segment.export(file_path, format="mp3", bitrate="128k")
            logging.info(f"Audio saved to {file_path}")
    except exception as e:
        logging.error(f"An error occurred: {e}")

audio_filePath = "patient_test.mp3"    
# record_audio(file_path=audio_filePath)

    #setup speech to text stt-model for transcription
import os
from groq import Groq
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
stt_model = "whisper-large-v3"


def transcribe_with_groq(stt_model,audio_filePath,GROQ_API_KEY):
    client = Groq(api_key=GROQ_API_KEY)
    audio_file = open(audio_filePath, "rb")
    transcription = client.audio.transcriptions.create(
        model=stt_model,
        file=(audio_filePath, audio_file.read()),
        language="en",
        response_format="verbose_json",
    )
    return transcription.text


