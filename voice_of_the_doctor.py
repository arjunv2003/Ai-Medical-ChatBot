#setup the text to speech model (GTTS)
import os
from gtts import gTTS

def text_to_speech_gtts_old(input_text, output_file_path):
    language = "en"

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False,
        tld='co.uk'
    )
    audioobj.save(output_file_path)

# input_text = "Hi I am Your Doctor, How can I help you today?"
# text_to_speech_gtts_old(input_text,"gtts_testing.mp3")    


#setup the text to speech model (ElevenLabs)

import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_elevenlabs_old(input_text,output_file_path):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text = input_text ,
        voice = "Aria - Sexy Female Villain Voice",
        output_format = "mp3_22050_32",
        model = "eleven_turbo_v2"
    )

    elevenlabs.save(audio,output_file_path)


# text_to_speech_elevenlabs_old(input_text,"elevenlabs_testing.mp3")


# use model for text output to voice
import subprocess
import platform

def text_to_speech_gtts(input_text, output_file_path):
    language = "en"

    audioobj = gTTS(
        text = input_text,
        lang = language,
        slow = False,
        tld='co.uk'
    )
    audioobj.save(output_file_path)
    os_name= platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_file_path])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', 'Start-Process', output_file_path])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_file_path])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error occured while playing audio: {e}")

# input_text = "Hi I am Your Doctor, How can I help you today?"
# text_to_speech_gtts(input_text,"gtts_testing_autoplay.mp3")    

def text_to_speech_elevenlabs(input_text,output_file_path):
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio = client.generate(
        text = input_text ,
        # voice = "Nikita - Youthful Hindi Voice",
        output_format = "mp3_22050_32",
        model = "eleven_turbo_v2"
    )

    elevenlabs.save(audio,output_file_path)    
    os_name= platform.system()
    try:
        if os_name == "Darwin":
            subprocess.run(['afplay', output_file_path])
        elif os_name == "Windows":
            subprocess.run(['powershell', '-c', 'Start-Process', output_file_path])
        elif os_name == "Linux":
            subprocess.run(['aplay', output_file_path])
        else:
            raise OSError("Unsupported OS")
    except Exception as e:
        print(f"Error occured while playing audio: {e}")


# text_to_speech_elevenlabs(input_text,"elevenlabs_testing_autoplay.mp3")