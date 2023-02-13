from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

firefox = webdriver.Firefox()

# response = firefox.get("https://www.python.org/")

# search_input = firefox.find_element("name", "q")
# search_input.send_keys("selenium")
# search_input.send_keys(Keys.ENTER)

# search_input = firefox.find_element(By.NAME, 'q')
# search_input.send_keys('selenium')
# search_input.submit()


def scrape(url):
    firefox.get(url)
    books = []
    for book in firefox.find_elements(By.CLASS_NAME, "product_pod"):
        new_item = {}
        new_item["title"] = (
            book.find_element(By.TAG_NAME, 'h3')
            .find_element(By.TAG_NAME, 'a')
            .get_attribute("innerHTML")
        )
        new_item["price"] = (
            book.find_element(By.CLASS_NAME, 'price_color')
            .get_attribute("innerHTML")
        )
        new_item["link"] = (
            book.find_element(By.CLASS_NAME, "image_container")
            .find_element(By.TAG_NAME, 'a')
            .get_attribute('href')
        )

        books.append(new_item)
    return books


firefox.get("https://books.toscrape.com/")
all_books = []
url2request = "https://books.toscrape.com/"

next_page_link = (
    firefox.find_element(By.CLASS_NAME, "next")
    .get_attribute("innerHTML")
)

while next_page_link:
    all_books.extend(scrape(url2request))
    try:
        url2request = (
            firefox.find_element(By.CLASS_NAME, "next")
            .find_element(By.TAG_NAME, "a")
            .get_attribute("href")
        )
    except NoSuchElementException:
        print("exception handled")
        break


print(all_books)
