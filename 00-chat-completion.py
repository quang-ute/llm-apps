import os
from groq import Groq
from rich import print
from dotenv import load_dotenv


# Remember to load the environment variables. You should have the Groq API Key in there :)
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq()
completion = client.chat.completions.create(
    model = "llama3-70b-8192",
    messages = [
    {
        "role":"system",
        "content":"You are a helpful AI assistant."
    },
    {
        "role":"user",
        "content":"Generate an essay to introduce relevant concepts in the realm of  Generative AI"
    }
]
)
print(completion)
#print(completion.choices[0].message.content)
