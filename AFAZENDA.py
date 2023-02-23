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
url_site = "https://www.globo.com/"

# Abrir a página desejada
driver.get(url_site)


# Take 5 screenshots every 5 seconds
for i in range(5):
    driver.save_screenshot(f"screenshot{i+1}.png")
    time.sleep(9)
    
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
