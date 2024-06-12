import requests
from bs4 import BeautifulSoup
import feedparser
import pandas as pd
from datetime import datetime

# Função para extrair notícias da Apple
def get_apple_news():
    url = 'https://www.apple.com/newsroom/rss-feed.rss'
    feed = feedparser.parse(url)
    apple_news = []
    for entry in feed.entries:
        published = entry.get('published', datetime.now().isoformat())
        apple_news.append({
            'title': entry.title,
            'link': entry.link,
            'published': published,
            'source': 'Apple'
        })
    return apple_news

# Função para extrair notícias do Google
def get_google_news():
    url = 'https://blog.google/rss'
    feed = feedparser.parse(url)
    google_news = []
    for entry in feed.entries:
        published = entry.get('published', None)
        google_news.append({
            'title': entry.title,
            'link': entry.link,
            'published': published,
            'source': 'Google'
        })
    return google_news

# Função para extrair notícias do NVIDIA
def get_nvidia_news():
    url = 'https://nvidianews.nvidia.com/releases.xml'
    feed = feedparser.parse(url)
    nvidia_news = []

    for entry in feed.entries:
        published = entry.get('published', entry.get('pubDate', None))
        nvidia_news.append({
            'title': entry.title,
            'link': entry.link,
            'published': published,
            'source': 'NVIDIA'
        })
    return nvidia_news

# Função principal para coletar todas as notícias
def collect_news():
    news = []
    news.extend(get_apple_news())
    news.extend(get_google_news())
    news.extend(get_nvidia_news())
    return news

# Função para salvar as notícias em um arquivo CSV
def save_news_to_csv(news, filename='news.csv'):
    df = pd.DataFrame(news)
    df.to_csv(filename, index=False)


if __name__ == '__main__':
    all_news = collect_news()
    save_news_to_csv(all_news)
    print(f"Saved {len(all_news)} news articles to news.csv")
