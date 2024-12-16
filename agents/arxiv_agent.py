import os
from swarm import Agent
from dotenv import load_dotenv

# Import the arXiv search tool
from tools.arxiv_tool import search_arxiv

# Load environment variables
load_dotenv()
MODEL = os.getenv('MODEL')

# arXiv Agent
arxiv_agent = Agent(
    name="arXiv Assistant",
    instructions="You help users find recent research articles on arXiv based on their search query. Provide a list of recent article titles related to the search term, sorted by submission date.",
    functions=[search_arxiv],
    model=MODEL
)