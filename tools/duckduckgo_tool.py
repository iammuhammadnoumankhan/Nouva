from duckduckgo_search import DDGS
from duckduckgo_search.exceptions import RatelimitException
import time

def search_duckduckgo(query, max_results=5):
    """Search DuckDuckGo for the given query and return titles of results."""
    ddgs = DDGS()
    try:
        results = ddgs.text(query, max_results=max_results)
        return [{"title": result["title"], "url": result["href"]} for result in results]
    except RatelimitException:
        print("Rate limit exceeded. Please wait before trying again.")
        time.sleep(5)  # Wait for 5 seconds before retrying or handling differently
        return []