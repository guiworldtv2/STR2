from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://youtube.com/")
titles = driver.find_elements(By.XPATH, '//*[@id="video-title"]')
views = driver.find_elements(By.XPATH, '//*[@id="metadata-line"]')

for i in range(len(views)):
    print(titles[i].text)
    print(views[i].text, '\n')

driver.close()
