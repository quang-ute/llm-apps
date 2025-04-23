from dotenv import load_dotenv
from litellm import completion
import os
from rich import print

load_dotenv()

api_key = os.environ["GROQ_API_KEY"]

def get_llm_response(message):
    response = completion(
        model="groq/qwen-qwq-32b",
        api_key = api_key,
        messages=message,
        stream=False
    )
    return response

messages = [
    {
        "role":"system",
        "content":"You are a helpful AI assistant"
    },
    {
        "role":"user",
        "content":"Why do we have alternating current?"
    }
]


response = get_llm_response(messages)
print(response)
#print(response.choices[0].message.content)