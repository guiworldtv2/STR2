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
chrome_options.add_argument("--window-size=1920,1080") # set screen size to 1920x1080
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_twitch = "https://affiliates.video.globo.com/affiliates/info"

# Abrir a página desejada
driver.get(url_twitch)

# Define a duração da gravação em segundos
duration = 15

# Inicia o processo ffmpeg para gravar a tela
cmd = f"ffmpeg -y -f avfoundation -r 30 -t {duration} -i :0 out.mp4"
process = subprocess.Popen(cmd.split())

# Aguarda a gravação terminar
time.sleep(duration)

# Encerra o processo ffmpeg
process.terminate()



    
    # Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(15)

try:
    # Obter o arquivo .m3u8
    # Pegando o log de requisições da aba Rede
    log_entries = driver.execute_script("return window.performance.getEntries();")

    # Buscando a primeira requisição que tem um arquivo .m3u8
    for entry in log_entries:
        if ".m3u8" in entry['name']:
            print(entry['name'])
            link = entry['name']
            break
    else:
        print("No .m3u8 files found in network log entries")

except Exception as e:
    print("Error occurred while trying to obtain .m3u8 file:")
    print(e)

# Fechando o driver
driver.quit()
