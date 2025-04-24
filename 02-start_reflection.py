import os
from groq import Groq
from rich import print
from dotenv import load_dotenv


# Remember to load the environment variables. You should have the Groq API Key in there :)
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq()

# First prompt
generation_chat_history = [
    {
        "role": "system",
        "content": 
        """
            You are a 10-year experience programmer tasked with generating high-quality python code.
            Your task is to Generate the best content possible for the user's request. 
        """
    },
    {   "role": "user",
        "content": 
        """
        Generate a python implementation of quicksort algorithm. 
        """
    }
]

# First generation
python_code = client.chat.completions.create(
    messages=generation_chat_history,
    model="llama3-70b-8192"
).choices[0].message.content

generation_chat_history.append(
    {
        "role": "assistant",
        "content": python_code
    }
)
print(python_code)



