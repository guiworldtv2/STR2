import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options

# URL da página desejada
url_twitch = "https://www.twitch.tv/directory/game/Just%20Chatting"

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Abrir a página desejada
driver.get(url_twitch)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Obter o conteúdo da página
html_content = driver.page_source

# Encontrar os links e títulos dos primeiros quatro vídeos encontrados
soup = BeautifulSoup(html_content, "html.parser")
videos = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link", href=True)[:4]
links = ["https://www.twitch.tv" + video.get("href") for video in videos]
titles = [video.find("h3").get("title") for video in videos]
thumbnails = [video.find("img").get("src") for video in videos]

# Fechar o driver
driver.quit()

# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

try:
    # Get LISTA4.m3u8
    with open('./TWITCH.m3u8', 'w') as f:
        f.write("#EXTM3U\n")
        for i in range(len(links)):
            streams = streamlink.streams(links[i])
            url = streams['best'].url
            f.write(f"#EXTINF:-1 tvg-id='{titles[i]}' tvg-logo='{thumbnails[i]}',{titles[i]}\n")
            f.write(f"{url}\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")

