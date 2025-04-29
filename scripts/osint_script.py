import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = "https://news.ycombinator.com/"
    response = requests.get(url)
    print("Page loaded successfully")

    soup = BeautifulSoup(response.text, 'html.parser')
    titles = soup.select('.titleline > a')  # Updated selector

    print("Top News Headlines:")
    for i, title in enumerate(titles[:10], 1):
        print(f"{i}. {title.text}")

fetch_news()
