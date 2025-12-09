import os
from openai import OpenAI
from dotenv import load_dotenv
load_dotenv(override=True)

# using the free-tier google api version 
# GEMINI_BASE_URL = "https://generativelanguage.googleapis.com/v1beta/openai/"
# google_api_key = os.getenv("GOOGLE_API_KEY")
# gemini = OpenAI(base_url=GEMINI_BASE_URL, api_key=google_api_key)
# response = gemini.chat.completions.create(
#     model="gemini-2.5-flash", # Specify the Gemini model
#     messages=[
#         {"role": "user", "content": "Explain how this works"},
#     ],
# )
# print(response.choices[0].message.content)

OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key="anything")
response = ollama.chat.completions.create(model="llama3.2", messages=[{"role":"sytem", "content": "you are maths guru."},{"role":"user", "content": "who are you?"},{"role":"user", "content": "solve this trignometric eqations 1) 10 = sin(Theta) 2) 10 = 10sin(Theta) what are the value of thetha in both the equations?"}])
print(response.choices[0].message.content)