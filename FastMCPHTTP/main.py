from fastmcp import FastMCP
import feedparser


mcp = FastMCP(name="Freecodecamp Feed Searcher")


@mcp.tool()
def fcc_news_search(query:str,max_results:int=3):   
    """
    search freecodecamp feed using rss by title/description.
    :param query: Description
    :type query: str
    :param max_results: Description
    :type max_results: int
    """

    feed = feedparser.parse("https://www.freecodecamp.org/news/rss")

    results = []

    query_lower = query.lower()

    for entry in feed.entries:
        title = entry.get("title","")
        description = entry.get("description","")
        if query_lower in title.lower() or query_lower in description.lower():
            results.append({"title":title,"url" :entry.get("link","")})
        if len(results) >= max_results:
            break #unlikely to happen 

    return results or [{"message":"No results found"}]


@mcp.tool()
def fcc_youtube_search(query:str,max_results:int= 3):
    """searcg freecodecamp youtube channel via rss by title"""
    feed = feedparser.parse("https://youtube.com/feeds/videos.xml?channel_id=UC8butISFwT-Wl7EV0hUK0BQ")

    results = []
    query_lower = query.lower()

    for entry in feed.entries:
        title = entry.get("title","")
        if query_lower in title.lower():
            results.append({"title":title,"url":entry.get("link","")})
        if len(results) >= max_results:
            break
    return results or [{"message":"No results found"}]

@mcp.tool()
def fcc_secret_msg():
    """returns a secret message"""

    return "keep exploring! and happy coding"

if __name__ == "__main__":
    mcp.run()  
