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
    # Start with manager agent
    agent = manager_agent

    while True:
        user_input = input(f"\n\n{GREEN}**You**{RESET}: ")
        tool_use = orchestrator(user_input)
        # print(tool_use)
        user_input =  f' using {tool_use} agent answer, ' + user_input 
        # print(user_input)

        # Exit condition
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"{GREEN}Goodbye!{RESET}")
            break

        messages.append({"role": "user", "content": user_input})

        # Run the current agent
        response = client.run(agent=agent, messages=messages)
        messages = response.messages
        agent = response.agent
        
        # Print response
        pretty_print_messages(messages)

if __name__ == "__main__":
    main()