from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Setup Chrome browser (headless mode optional)
options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # uncomment for headless mode

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Open target website
driver.get("http://quotes.toscrape.com")

# Scrape all quotes on the first page
quotes = driver.find_elements(By.CLASS_NAME, "quote")

for quote in quotes:
    text = quote.find_element(By.CLASS_NAME, "text").text
    author = quote.find_element(By.CLASS_NAME, "author").text
    print(f'"{text}" - {author}')

# Close the browser
driver.quit()