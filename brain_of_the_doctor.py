#setup Groq API key
import os
GROQ_API_KEY = os.environ.get("GROQ_API_KEY")

#convert the image to base64
import base64

# image_path = "versicolor.jpg"

def encode_image(image_path):
    image_file = open(image_path, "rb")
    return base64.b64encode(image_file.read()).decode("utf-8")

    
#setup Multimodal LLM

from groq import Groq
query = "is there something wring with the me? give me the solution"
model = "meta-llama/llama-4-scout-17b-16e-instruct"
def analyze_image_with_query(query,model,encoded_img):
    client = Groq()
    messages = [
        {
            "role":"user",
            "content":[
                {
                    "type":"text",
                    "text":query
                },
                {
                    "type":"image_url",
                    "image_url":{
                    "url" : f"data:image/jpeg;base64,{encoded_img}",
                    }
                },
            ],
        }
    ]

    chat_completion = client.chat.completions.create(
        messages = messages,
        model = model
    )
    
    return (chat_completion.choices[0].message.content)