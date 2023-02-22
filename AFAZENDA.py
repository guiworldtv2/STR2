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
chrome_options.add_argument("user-data-dir=https://drive.google.com/drive/folders/1VkhVPGRZ0j5h937AwjpIKBAupKbESb83?usp=sharing") # replace with the path to the Chrome profile

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

# Encontrar o link .m3u8 na página
start_index = html_content.find("var urlLive = '") + 15
end_index = html_content.find("';", start_index)
link = html_content[start_index:end_index]
print(link)

# Close the driver
driver.quit()
