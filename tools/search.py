try:
    from ddgs import DDGS
except ImportError:
    from duckduckgo_search import DDGS


def _duckduckgo_search(query, max_results=5):
    links = []

    with DDGS() as ddgs:
        try:
            results = ddgs.text(
                query,
                max_results=max_results,
                safesearch="moderate"
            )
        except TypeError:
            results = ddgs.text(
                keywords=query,
                max_results=max_results,
                safesearch="moderate"
            )

        for result in results:
            href = result.get("href")
            if href and href.startswith("http"):
                links.append(href)

    return links


def web_search(queries):
    urls = []

    for query in queries:
        try:
            urls.extend(_duckduckgo_search(query, max_results=5))
        except Exception:
            continue

    deduped_urls = []
    seen = set()
    for url in urls:
        if url not in seen:
            seen.add(url)
            deduped_urls.append(url)

    return deduped_urls