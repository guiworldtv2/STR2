from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os
import subprocess
from bs4 import BeautifulSoup


# URL da página desejada
url_playplus = "https://www.playplus.com/live/liveEvent/249"

# Criando as opções para o Google Chrome
options = Options()
options.add_argument(f"user-data-dir=/home/codespace/.config/google-chrome/MEU PROFILE")  # caminho do perfil do usuário
options.add_argument("--start-maximized")  # maximizar a janela do navegador
options.add_argument("--disable-infobars")  # desabilitar a barra de informações do Chrome
options.add_argument("--no-sandbox")


# Instanciando o driver do Google Chrome
driver = webdriver.Chrome(options=options)

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
