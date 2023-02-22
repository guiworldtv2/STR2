import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")


# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_playplus = "https://www.playplus.com/live/liveEvent/249"

# Abrir a página desejada
driver.get(url_playplus)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Get the page source to find the .m3u8 link
html_content = driver.page_source


# Close the driver
driver.quit()
