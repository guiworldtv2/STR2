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
url_twitch = "https://www.twitch.tv/jolyn"

# Abrir a página desejada
driver.get(url_twitch)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Obter o arquivo .m3u8
# Pegando o log de requisições da aba Rede
log_entries = driver.execute_script("return window.performance.getEntries();")

# Buscando a primeira requisição que tem um arquivo .m3u8
for entry in log_entries:
    if ".m3u8" in entry['name']:
        print(entry['name'])
        link = entry['name']
        break

# Fechando o driver
driver.quit()
