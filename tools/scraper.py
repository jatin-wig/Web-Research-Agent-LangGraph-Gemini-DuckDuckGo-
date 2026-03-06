import requests
from bs4 import BeautifulSoup

def scrape_urls(urls):
    contents = []

    for url in urls[:12]:
        try:
            html = requests.get(url, timeout=6).text
            soup = BeautifulSoup(html, "html.parser")

            for tag in soup(["script", "style", "noscript"]):
                tag.extract()

            text = soup.get_text(separator=" ")
            cleaned = " ".join(text.split())

            contents.append(cleaned[:10000])
        except:
            continue

    return contents