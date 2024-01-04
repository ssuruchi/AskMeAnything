import requests
from bs4 import BeautifulSoup

def get_article_text(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        article_content = soup.find("div", class_ = "a-wrapper")
        if article_content:
            article_text = article_content.get_text()
            return article_text
        else:
            return "Article content was not found on the page"
    else:
        return f"Failed to retrieve page. Status Code: {response.status_code}"
    