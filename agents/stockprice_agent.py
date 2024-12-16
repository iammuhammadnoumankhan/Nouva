import os
from swarm import Agent
from dotenv import load_dotenv

# Import the stock price tool
from tools.stockprice_tool import get_stock_price

# Load environment variables
load_dotenv()
MODEL = os.getenv('MODEL')

# Stock Price Agent
stockprice_agent = Agent(
    name="Stock Price Assistant",
    instructions="You provide the latest stock price for a given ticker symbol using the yfinance library. Use standard ticker symbols (e.g., AAPL for Apple). Provide only the stock price information without additional commentary.",
    functions=[get_stock_price],
    model=MODEL
)