# Gradio for Ui
import os
import gradio as gr

from brain_of_the_doctor import encode_image,analyze_image_with_query
from voice_of_the_patient import record_audio, transcribe_with_groq
from voice_of_the_doctor import text_to_speech_elevenlabs,text_to_speech_gtts

system_prompt="""You have to act as a professional doctor, i know you are not but this is for learning purpose. 
            What's in this image?. Do you find anything wrong with it medically? 
            If you make a differential, suggest some remedies for them. Donot add any numbers or special characters in 
            your response. Your response should be in one long paragraph. Also always answer as if you are answering to a real person.
            Donot say 'In the image I see' but say 'With what I see, I think you have ....'
            Dont respond as an AI model in markdown, your answer should mimic that of an actual doctor not an AI bot, 
            Keep your answer concise (max 2 sentences). No preamble, start your answer right away please"""

def process_inputs(audio_filepath, image_filepath):
    #error handling
    if not audio_filepath and not image_filepath:
        return "", "", text_to_speech_gtts(input_text="I can definitely help you ,Please upload an image and tell me what happened", output_file_path="final.mp3")

    if not audio_filepath:
        return "", "", text_to_speech_gtts(input_text="Could you tell me what happened by tapping on record button", output_file_path="final.mp3")
    
    speech_to_text_output = transcribe_with_groq(GROQ_API_KEY=os.environ.get("GROQ_API_KEY"), 
                                                 audio_filePath=audio_filepath, 
                                                 stt_model="whisper-large-v3")
  
    # Handle the image input 
    if image_filepath:
        doctor_response = analyze_image_with_query(query=system_prompt+speech_to_text_output, encoded_img=encode_image(image_filepath), model="meta-llama/llama-4-scout-17b-16e-instruct")
    else:
        doctor_response = "No image provided for me to analyze"

    voice_of_doctor = text_to_speech_gtts(input_text=doctor_response, output_file_path="final.mp3") 

    return speech_to_text_output, doctor_response, voice_of_doctor


# Create the interface
iface = gr.Interface(
    fn=process_inputs,
    inputs=[
        gr.Audio(sources=["microphone"], type="filepath"),
        gr.Image(type="filepath")
    ], 
    outputs=[
        gr.Textbox(label="Speech to Text"),
        gr.Textbox(label="Doctor's Response"),
        gr.Audio("Temp.mp3")
    ],
    title="AI Doctor with Vision and Voice Your Health Assistant",
    description="This is a Chat Bot made by Arjun that allows you to record your voice, upload an image, and get a response from an AI doctor. It will analyze the image and provide a response based on the audio input.",
    theme="default",
    allow_flagging="never",
)

# iface.launch(debug=True)


port = int(os.environ.get("PORT", 7860))  # Render sets this automatically
interface.launch(server_name="0.0.0.0", server_port=port)
