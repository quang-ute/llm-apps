import os
from litellm import completion
from rich import print
from dotenv import load_dotenv


# Remember to load the environment variables. You should have the Groq API Key in there :)
load_dotenv()

# First prompt
generation_chat_history = [
    {
        "role": "system",
        "content": 
        """
            You are a programmer tasked with generating high quality python code.
            Your task is to Generate the best content possible for the user's request. 
        """
    },
    {   "role": "user",
        "content": 
        """
        Generate a python implementation of AVL Tree.
        """
    }
]
api_key = os.environ["GEMINI_API_KEY"]

def get_llm_response(message):
    response = completion(
        model = "gemini/gemini-2.5-flash-preview-04-17",
        messages=message,
        stream=False
    )
    return response

tree_code = get_llm_response(generation_chat_history)
generation_chat_history.append(
    {
        "user":"assitant",
        "content":tree_code
    }
)
print(tree_code)