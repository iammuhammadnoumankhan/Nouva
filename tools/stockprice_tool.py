import yfinance as yf

def get_stock_price(ticker):
    """Fetch the latest stock price for a given ticker."""
    print(f"Running stock price function for {ticker}...")
    
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period="1d")
    
    if not stock_info.empty:
        latest_price = stock_info['Close'].iloc[-1]
        return f"The latest stock price for {ticker} is {latest_price}."
    else:
        return f"Could not retrieve stock price for {ticker}."