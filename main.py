import os
from dotenv import load_dotenv
from swarm import Swarm

# Import agents
from agents.manager_agent import manager_agent

# Import utilities
from utils.helpers import pretty_print_messages, orchestrator

# Load environment variables
load_dotenv()

os.environ["OPENAI_BASE_URL"] = os.getenv('OPENAI_BASE_URL')
os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
os.environ["MODEL"] = os.getenv('MODEL')



# ANSI escape codes
GREEN = "\033[92m"
RESET = "\033[0m"

def main():
    # Initialize Swarm client
    client = Swarm()

    print(f"{GREEN}Welcome to the Nouva Personal Assistant! \nType 'exit' to end the conversation.{RESET}")
    messages = []

    system_message = '''You are Nouva, a modular and privacy-focused AI assistant built on an agentic framework. Your primary goal is to assist users efficiently while ensuring their data privacy. You operate using a swarm of specialized agents, each designed for tasks like research, Python code execution, web searches, stock price tracking, weather updates, and more.
        Respond clearly, concisely, and helpfully to user queries. When necessary, route tasks to the appropriate agent based on its expertise, and notify the user if additional context or clarification is needed. Emphasize the privacy-first and modular nature of the system, and suggest new tools or agents if they could enhance the user's experience.
        Always prioritize user satisfaction, adapt to their needs, and strive to make complex tasks simple and accessible. If unsure, clarify rather than assume.'''

    messages.append({"role": "system", "content": system_message})
    # Start with manager agent
    agent = manager_agent

    while True:
        user_input = input(f"\n\n{GREEN}**You**{RESET}: ")

        messages.append({"role": "user", "content": user_input})

        # helper function
        tool_use = orchestrator(user_input)
        user_input =  f' using {tool_use} agent answer, ' + user_input 

        # Exit condition
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"{GREEN}Goodbye!{RESET}")
            break

        # Run the current agent
        response = client.run(agent=agent, messages=messages)
        # messages = response.messages
        # agent = response.agent
        # print(response.messages[0]['content'])
        messages.append({"role": "assistant", "content": response.messages[0]['content']})
        
        # Print response
        pretty_print_messages(response.messages)

if __name__ == "__main__":
    main()