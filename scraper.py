# scraper.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import json

def scrape_quotes():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Runs Chrome in headless mode
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("http://quotes.toscrape.com")
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "quote")))

    all_quotes = []
    quotes = driver.find_elements(By.CLASS_NAME, "quote")
    for quote in quotes:
        text = quote.find_element(By.CLASS_NAME, "text").text
        author = quote.find_element(By.CLASS_NAME, "author").text
        all_quotes.append({"text": text, "author": author})

    driver.quit()

    with open("quotes.json", "w", encoding="utf-8") as f:
        json.dump(all_quotes, f, indent=4, ensure_ascii=False)

    return all_quotes