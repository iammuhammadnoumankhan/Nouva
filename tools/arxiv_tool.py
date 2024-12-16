import arxiv

def search_arxiv(query, max_results=10):
    """Search for articles on arXiv based on a query."""
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.SubmittedDate
    )
    
    results = client.results(search)
    return [r.title for r in results]