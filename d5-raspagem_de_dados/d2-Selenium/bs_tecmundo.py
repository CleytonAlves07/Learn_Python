import requests
from bs4 import BeautifulSoup
from rich import print


def get_html_soup(url):
    page = requests.get(url)
    html_page = page.text

    soup = BeautifulSoup(html_page, "html.parser")
    soup.prettify()
    return soup


def get_page_news(soup):
    news = []

    for post in soup.find_all('article',
                              {'class': 'tec--card tec--card--medium'}):
        item = {}
        item['tag'] = post.find('div', {'class': 'tec--card__info'}).a.string
        item['title'] = post.find('h3', {'class': 'tec--card__title'}).a.string
        item['link'] = post.find('h3', {'class': 'tec--card__title'}).a['href']
        item['date'] = post.find(
            'div', {'class': 'tec--timestamp__item z--font-semibold'}).string
        item['time'] = post.find(
            'div', {'class': 'z--truncate z-flex-1'}).string
        news.append(item)
    return news


link = "https://www.tecmundo.com.br/novidades"
url_path = get_page_news(get_html_soup(link))

print(url_path)
