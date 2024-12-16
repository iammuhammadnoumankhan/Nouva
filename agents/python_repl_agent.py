import os
from swarm import Agent
from dotenv import load_dotenv
from langchain_core.tools import Tool

# Import the Python REPL tool
from tools.python_repl_tool import execute_python_code

# Load environment variables
load_dotenv()
MODEL = os.getenv('MODEL')

# Create the Python REPL tool
repl_tool = Tool(
    name="python_repl",
    description="A Python shell. Use this to execute Python commands. Input should be a valid Python command. If you want to see the output of a value, you should print it out with `print(...)`.",
    func=execute_python_code,
)

# Python REPL Agent
python_repl_agent = Agent(
    name="Python REPL Assistant",
    instructions="You can execute any valid Python code. Ensure to print the output if you want to see it. Be cautious and precise with code execution.",
    functions=[execute_python_code],
    model=MODEL,
    tools=[repl_tool]  # Add the Python REPL tool to the agent's tools list
)