import os
from swarm import Agent
from dotenv import load_dotenv

# Import the DuckDuckGo search tool
from tools.duckduckgo_tool import search_duckduckgo

# Load environment variables
load_dotenv()
MODEL = os.getenv('MODEL')

# DuckDuckGo Agent
duckduckgo_agent = Agent(
    name="DuckDuckGo Assistant",
    instructions="You help users find information by searching the internet. Provide relevant search results including titles and URLs based on the user's query.",
    functions=[search_duckduckgo],
    model=MODEL
)