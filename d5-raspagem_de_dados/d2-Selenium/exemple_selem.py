from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

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

        print(new_item)


scrape("https://books.toscrape.com/")
