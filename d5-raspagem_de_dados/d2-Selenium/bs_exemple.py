import requests
from bs4 import BeautifulSoup
from rich import print


url = "https://quotes.toscrape.com"
page = requests.get(url)
html_content = page.text
soup = BeautifulSoup(html_content, 'html.parser')


# print(soup.prettify())

title = soup.title
# print(title)

# print(title.name)
# print(title.string)
# print(type(title.string))

# footer = soup.footer

# print(footer['class'])

# print(soup.find_all('p'))

# print(soup.find(id="quote"))

# print(soup.get_text())

print(soup.find_all('div', {'class', 'quote'}))
