import streamlink
import subprocess

import time
import os
import subprocess
from selenium import webdriver
from bs4 import BeautifulSoup

while True:
    try:
        # URL da página desejada
        url_twitch = "https://www.twitch.tv/search?term=big%20brother"

        # Instanciando o driver do firefox
        driver = webdriver.Firefox()

        # Abrir a página desejada
        driver.get(url_twitch)

        # Aguardar alguns segundos para carregar todo o conteúdo da página
        time.sleep(5)

        # Obter o conteúdo da página
        html_content = driver.page_source

        # Encontrar o link do primeiro canal encontrado
        soup = BeautifulSoup(html_content, "html.parser")
        link = "https://www.twitch.tv" + soup.find("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv tw-link").get("href")

        # Fechar o driver
        driver.quit()

        print(link)
        
        
        # Install streamlink
subprocess.run(["pip", "install", "--user", "--upgrade", "streamlink"])

# Get LISTA4.m3u8
with open("./BBVIPALBANIA.m3u8", "w") as f:
    f.write("#EXTM3U\n")
    f.write("#EXT-X-VERSION:3\n")
    f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")
    



            # Run streamlink and get the stream URL
            result = subprocess.run(["streamlink", "--twitch-disable-ads","--twitch-disable-reruns","--url", "--default-stream", "--stream-url", link, "best"], capture_output=True, text=True)

            if result.returncode == 0:
                stream_url = result.stdout.strip()
                f.write(stream_url + "\n")
            else:
                f.write("https://raw.githubusercontent.com/guiworldtv/STR2/main/VideoOFFAir.m3u8\n")
