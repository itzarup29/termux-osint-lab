import requests
from bs4 import BeautifulSoup

def fetch_news():
    url = 'https://news.ycombinator.com/'  # Example site (Hacker News)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    headlines = soup.find_all('a', class_='storylink')

    print("Top News Headlines:")
    for i, headline in enumerate(headlines[:10]):  # Limit to 10 headlines
        print(f"{i + 1}. {headline.text} - {headline['href']}")

if __name__ == "__main__":
    fetch_news()
