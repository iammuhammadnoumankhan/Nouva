import asyncio
from ollama import AsyncClient

# Define the host and model parameters.
HOST = "http://10.4.136.182:11434"  # http://localhost:11434
MODEL = 'llama3.2'


# ANSI escape code for green text.
GREEN = "\033[92m"  # Bright green color
RESET = "\033[0m"   # Reset to default color

# Maintain the conversation history.
conversation_history = []

# Function to handle the chat interactions.
async def chat(query):
    # Append the user query to the conversation history.
    conversation_history.append({'role': 'user', 'content': query})

    print(f"{GREEN}**Assistant**:{RESET}")

    # Create the client and stream the response.
    async for part in await AsyncClient(host=HOST).chat(model=MODEL, messages=conversation_history, stream=True):
        print(part['message']['content'], end='', flush=True)

    # Append the assistant's response to the history.
    conversation_history.append({'role': 'assistant', 'content': part['message']['content']})

# Main loop to handle user interactions.
def main():
    print(f"{GREEN}Welcome to the Nouva Personal Assistant! \nType 'exit' to end the conversation.{RESET}")
    while True:
        # Get user input.
        query = input(f"\n\n{GREEN}**You**{RESET}: ")

        # Break the loop if the user wants to exit.
        if query.lower() in ['exit', 'quit', 'bye']:
            print(f"{GREEN}Goodbye!{RESET}")
            break

        # Run the chat function asynchronously.
        asyncio.run(chat(query))

# Start the main function.
if __name__ == "__main__":
    main()