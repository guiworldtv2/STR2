from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import subprocess
from bs4 import BeautifulSoup
import streamlink
import subprocess
import time
import os
from selenium.webdriver.common.action_chains import ActionChains



# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument(f"user-data-dir=https://drive.google.com/drive/folders/1VkhVPGRZ0j5h937AwjpIKBAupKbESb83?usp=sharing")   # caminho do perfil do usuário

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_playplus = "https://www.playplus.com/live/liveEvent/249"

# Abrir a página desejada
driver.get(url_playplus)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Obter o conteúdo da página
html_content = driver.page_source

# Encontrar o link .m3u8 na página
start_index = html_content.find("var urlLive = '") + 15
end_index = html_content.find("';", start_index)
link = html_content[start_index:end_index]
print(link)

# Fechar o driver
driver.quit()
