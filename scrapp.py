from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import pandas as pd
import time
import requests

# Set up Chrome options
s = requests.Session()

options = Options()
options.add_argument("--headless") # run Chrome in headless mode
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-browser-side-navigation")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-extensions")
options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36')

# Set up Selenium service
service = Service('/path/to/chromedriver') # Replace with path to your chromedriver
driver = webdriver.Chrome(service=service, options=options)

# Navigate to the webpage
url = 'https://bg05.t1games.live/game/crash'
driver.get(url)

# Wait for the page to load
time.sleep(5)

# Extract page content using BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')
valores = soup.find_all('div', class_=re.compile('sc-f9c11e17-0 fmKPXU point'))

print(valores)

# Close the browser window and the service
driver.quit()
service.stop()
