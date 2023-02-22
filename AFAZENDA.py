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
chrome_options.add_argument("--window-size=1280,720") # set screen size to 1920x1080

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_playplus = "https://globoplay.globo.com/agora-na-tv/"

# Abrir a página desejada
driver.get(url_playplus)

# Take 5 screenshots every 5 seconds
for i in range(5):
    driver.save_screenshot(f"screenshot{i+1}.png")
    time.sleep(6)
    
    # Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Get the page source to find the .m3u8 link
html_content = driver.page_source


# Close the driver
driver.quit()
