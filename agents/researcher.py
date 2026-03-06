from tools.search import web_search
from tools.scraper import scrape_urls

def research_node(state):
    urls = web_search(state["queries"])
    raw_content = scrape_urls(urls)

    return {
        "urls": urls,
        "raw_content": raw_content
    }