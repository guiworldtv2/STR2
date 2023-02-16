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
url_twitch = "https://www.twitch.tv/"

# Abrir a página desejada
driver.get(url_twitch)

import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains

# Configurando as opções do Chrome
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_twitch = "https://www.twitch.tv/"

# Abrir a página desejada
driver.get(url_twitch)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Scroll até o final da página usando ActionChains
while True:
    try:
        # Encontrar o último vídeo na página
        last_video = driver.find_element_by_xpath("//a[@class='ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link'][last()]")
        # Scroll até o último vídeo
        actions = ActionChains(driver)
        actions.move_to_element(last_video).perform()
        time.sleep(1)
    except:
        break
        
        
# Obter o conteúdo da página novamente após o scroll até o final
html_content = driver.page_source

# Encontrar os links e títulos dos vídeos encontrados
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link", href=True)
    links = ["https://www.twitch.tv" + video.get("href") for video in videos]
    channels = [video.find("p", {"data-a-target": "preview-card-channel-link", "class": "CoreText-sc-1txzju1-0 jiepBC"}).get("title") for video in videos]
    titles = [video.find("h3", class_="CoreText-sc-1txzju1-0 eJuFGD").get("title") for video in videos]
    
    # Encontrar as URLs das thumbnails para cada vídeo
    thumbnails = []
    for video in videos:
        channel_name = video.get("href")[1:]
        thumbnail_url = f"https://static-cdn.jtvnw.net/previews-ttv/live_{channel_name}-214x120.jpg"
        thumbnails.append(thumbnail_url)

except Exception as e:
    print(f"Erro: {e}")
finally:
    # Fechar o driver
    driver.quit()


# Instalando o streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

# Obter a playlist e escrever no arquivo
try:
    with open('./TWITCHPLAY.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
        for i, link in enumerate(links):
            # Get the stream information using streamlink
            streams = streamlink.streams(link)
            url = streams['best'].url

            # Get the channel name and title
            channel = channels[i]
            title = titles[i]

            # Get the thumbnail
            thumbnail = ""
            try:
                thumbnail = soup.find("a", href=link).find("img", class_="search-result-card__img tw-image").get("src")
            except:
                thumbnail = "https://via.placeholder.com/214x120.png?text=No+Thumbnail"

            # Write the stream information to the file
            title = channels[i]
            thumbnail = thumbnails[i]

            f.write(f"#EXTINF:-1 tvg-id='{title}' group-title=\"TWITCH\",{title}\n")           
            f.write(f"#EXTGRP:{title}\n")  
            f.write(f"#EXTIMG:{thumbnail}\n")
            f.write(f"{url}\n")
            f.write("\n")

