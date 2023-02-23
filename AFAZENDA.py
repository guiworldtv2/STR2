from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL da página de login
url_playplus_login = "https://www.rtve.es/play/videos/directo/deportes/baloncesto-espana-islandia-clasificacion/"

# Criando as opções para o chrome

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080") # set screen size to 1920x1080
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do chrome
driver = webdriver.Chrome(options=options)

# Abrir a página de login do PlayPlus
driver.get(url_playplus_login)



# Esperando a página ser carregada após clicar no perfil do usuário
time.sleep(10)

# URL da página desejada para extração da .m3u8
url_playplus = "https://www.rtve.es/play/videos/directo/deportes/baloncesto-espana-islandia-clasificacion/"

# Abrir a página desejada após o login
driver.get(url_playplus)

# Esperando o vídeo ser carregado e reproduzido
time.sleep(5)

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

# Fechar o driver
driver.quit()
