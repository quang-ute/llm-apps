import os
from groq import Groq
from rich import print
from dotenv import load_dotenv


# Remember to load the environment variables. You should have the Groq API Key in there :)
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")
client = Groq()

# Step 1 - First prompt
generation_chat_history = [
    {
        "role": "system",
        "content": 
        """
            You are an NASM programmer tasked with generating high quality NASM code.
            Your task is to Generate the best content possible for the user's request. 
            If the user provides critique,respond with a revised version of your previous attempt.
        """
    },
    {   "role": "user",
        "content": 
        """
        Generate a NASM implementation of the string reverse algorithm. The string will be printed twice:
        - before reverse and after reverse. Program must use function for repeated activities.
        """
    }
]

# First generation
nasm_code = client.chat.completions.create(
    messages=generation_chat_history,
    model="llama3-70b-8192"
).choices[0].message.content

generation_chat_history.append(
    {
        "role": "assistant",
        "content": nasm_code
    }
)
print(nasm_code)

# Step 2 - Reflection
reflection_chat_history = [
    {
        "role": "system",
        "content": """You are Andrej Karpathy, an experienced computer scientist. 
        You are tasked with generating critique and recommendations for the user's code""",
    },
    {
        "role": "user",
        "content": nasm_code
    }
]
# Generation of critique
critique = client.chat.completions.create(
    messages=reflection_chat_history,
    model="llama3-70b-8192"
).choices[0].message.content

print(critique)

generation_chat_history.append(
    {
        "role": "user",
        "content": critique
    }
)

# Step 4 - New generation starts
essay = client.chat.completions.create(
    messages=generation_chat_history,
    model="llama3-70b-8192"
).choices[0].message.content

print(essay)
