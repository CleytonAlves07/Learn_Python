from selenium import webdriver


firefox = webdriver.Firefox()

response = firefox.get("https://www.python.org/")
