import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import youtube_dl

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# URL da página desejada
url_youtube = "https://www.youtube.com/results?search_query=podcast&sp=CAISAhgC"

# Abrir a página desejada
driver.get(url_youtube)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Scroll to the bottom of the page using ActionChains
while True:
    try:
        # Find the last video on the page
        last_video = driver.find_element_by_xpath("//a[@class='ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link'][last()]")
        # Scroll to the last video
        actions = ActionChains(driver)
        actions.move_to_element(last_video).perform()
        time.sleep(1)
    except:
        break
        
        
# Get the page source again after scrolling to the bottom
html_content = driver.page_source

time.sleep(5)

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", id="video-title", class_="yt-simple-endpoint style-scope ytd-video-renderer")
    links = ["https://www.youtube.com" + video.get("href") for video in videos]
    titles = [video.get("title") for video in videos]
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()




# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'youtube-dl'])


time.sleep(5)

# Define as opções para o youtube-dl
ydl_opts = {
    'format': 'best',   # Obtém a melhor qualidade
    'merge_output_format': 'm3u8',  # Obtém a url com o formato .m3u8
    'write_all_thumbnails': True,  # Grava todas as thumbnails em arquivos separados
    'outtmpl': '%(id)s.%(ext)s',  # Nome do arquivo de saída
}

try:
    with open('./YOUTUBEPLAY.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
        for i, link in enumerate(links):
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                # Obtém informações do vídeo com o youtube-dl
                info_dict = ydl.extract_info(link, download=False)

                # Obtém a url do vídeo com o formato .m3u8
                url = info_dict['url']

                # Obtém a thumbnail do vídeo
                thumbnail_url = info_dict['thumbnails'][0]['url']

                # Grava a thumbnail em um arquivo
                thumbnail_filename = f"{info_dict['id']}.jpg"
                with open(thumbnail_filename, 'wb') as thumbnail_file:
                    thumbnail_file.write(ydl.urlopen(thumbnail_url).read())

                # Escreve as informações do vídeo no arquivo .m3u8
                title = titles[i]
                f.write(f"#EXTINF:-1 group-title=\"YOUTUBE\" tvg-logo= "thumbnail_filename", {title}\n")
                f.write(f"#EXTVLCOPT:program=128\n")  # Define o programa para 128
                f.write(f"{url}\n\n")
                f.write(f"#EXTVLCOPT:thumbnail-file={thumbnail_filename}\n")  # Adiciona o caminho para o arquivo da thumbnail
                f.write("\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")
