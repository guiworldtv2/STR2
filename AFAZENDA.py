from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import secrets 

# URL da página de login
url_playplus_login = "https://vimeo.com/598201688"

# Criando as opções para o chrome
options = Options()
options.add_argument("--window-size=1920,1080") # set screen size to 1920x1080
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# Instanciando o driver do chrome
driver = webdriver.Chrome(options=options)

# Abrir a página de login do PlayPlus
driver.get(url_playplus_login)

# Take 5 screenshots every 5 seconds
for i in range(5):
    driver.save_screenshot(f"screenshot{i+1}.png")
    time.sleep(9)


# Esperando a página ser carregada após clicar no perfil do usuário
time.sleep(10)


time.sleep(10)
#URL da página desejada para extração da .m3u8

url_playplus = "https://vimeo.com/598201688"
#Abrir a página desejada após o login

driver.get(url_playplus)
#Esperando a página ser carregada

# Obter o conteúdo da página
html_content = driver.page_source

# Pegando o log de requisições da aba Rede
log_entries = driver.execute_script("return window.performance.getEntries();")

# Buscando a primeira requisição que tem um arquivo .m3u8
for entry in log_entries:
    if ".m3u8" in entry['name']:
        print(entry['name'])
        link = entry['name']
        break
