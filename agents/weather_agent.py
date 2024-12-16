# agents/weather_agent.py
import os
from swarm import Agent
from dotenv import load_dotenv
from tools.weather_tool import get_weather

load_dotenv()
MODEL = os.getenv('MODEL')

weather_agent = Agent(
    name="Weather Assistant",
    instructions="You provide weather information for a given location using the provided tool, don't give any extra things.",
    functions=[get_weather],
    model=MODEL
)