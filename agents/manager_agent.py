import os
from swarm import Agent
from dotenv import load_dotenv

# Import other agents
from .weather_agent import weather_agent
from .stockprice_agent import stockprice_agent
from .arxiv_agent import arxiv_agent
from .duckduckgo_agent import duckduckgo_agent
from .python_repl_agent import python_repl_agent

# Load environment variables
load_dotenv()
MODEL = os.getenv('MODEL')

def transfer_to_weather_assistant(**args):
    """Transfer control to Weather Assistant."""
    print("Transferring to Weather Assistant...")
    return weather_agent

def transfer_to_stockprice_assistant(**args):
    """Transfer control to Stock Price Assistant."""
    print("Transferring to Stock Price Assistant...")
    return stockprice_agent

def transfer_to_arxiv_assistant(**args):
    """Transfer control to arXiv Assistant."""
    print("Transferring to arXiv Assistant...")
    return arxiv_agent

def transfer_to_duckduckgo_assistant(**args):
    """Transfer control to DuckDuckGo Assistant."""
    print("Transferring to DuckDuckGo Assistant...")
    return duckduckgo_agent

def transfer_to_python_repl_assistant(**args):
    """Transfer control to Python REPL Assistant."""
    print("Transferring to Python REPL Assistant...")
    return python_repl_agent

# Manager Agent
manager_agent = Agent(
    name="Manager Assistant",
    instructions="You help users by directing them to the right assistant. write now we have [transfer_to_weather_assistant, transfer_to_stockprice_assistant, transfer_to_arxiv_assistant, transfer_to_duckduckgo_assistant, transfer_to_python_repl_assistant]. transfer to the right assistant.",
    functions=[
        transfer_to_weather_assistant, 
        transfer_to_stockprice_assistant, 
        transfer_to_arxiv_assistant, 
        transfer_to_duckduckgo_assistant, 
        transfer_to_python_repl_assistant
    ],
    model=MODEL
)