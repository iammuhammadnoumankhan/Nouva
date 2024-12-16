# ANSI escape codes for colored output
GREEN = "\033[92m"  # Bright green color
RESET = "\033[0m"   # Reset to default color

# from ollama import Client
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
MODEL = os.getenv('MODEL')
HOST = os.getenv('OPENAI_BASE_URL')
API_KEY = os.getenv('OPENAI_API_KEY')


client = OpenAI(base_url=HOST, api_key=API_KEY)

def pretty_print_messages(messages):
    """Pretty print messages with color coding."""
    print(f"{GREEN}**Assistant**:{RESET}")

    for message in messages:
        if message["content"] is None:
            continue
        print(message["content"])

def orchestrator(query):

    completion = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You help users by directing them to the right assistant. write now we have [transfer_to_weather_assistant, transfer_to_stockprice_assistant, transfer_to_arxiv_assistant, transfer_to_duckduckgo_assistant, transfer_to_python_repl_assistant]. transfer to the right assistant. just give me the relavent assistant name from the list given. DONT GIVE ME ANY OTHER STUFF PLZZZ"},
            {
                "role": "user",
                "content": query
            }
        ]
    )

    # print(completion.choices[0].message.content)
    resp = completion.choices[0].message.content

    return resp.strip()