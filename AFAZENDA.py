import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import yt_dlp

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


# Get the playlist and write to file
try:
    with open('./YOUTUBEPLAY1.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
    for i, link in enumerate(links):
        with open('./YOUTUBEPLAY1.m3u', 'a') as f:
            # Get the stream information using yt-dlp
            with yt_dlp.YoutubeDL() as ydl:
                info = ydl.extract_info(link, download=False)
            if 'url' not in info:
                print(f"Erro ao gravar informações do vídeo {link}: 'url'")
                continue
            url = info['url']
            thumbnail_url = info['thumbnail']
            description = info.get('description', '')[:10]  # Use as primeiras 10 palavras da descrição ou menos
            # Write the stream information to the file
            title = titles[i]
            f.write(f"#EXTINF:-1 group-title=\"YOUTUBE2\" tvg-logo=\"{thumbnail_url}\",{title} - {description}\n")
            f.write(f"{url}\n\n")
            f.write("\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")
