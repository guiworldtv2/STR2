import streamlink
import subprocess
import time
import os
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")

# Instanciando o driver do Chrome
driver = webdriver.Chrome(options=chrome_options)

# Counter to name the downloaded videos
counter = 1

# loop through pages 1 to 2
for page in range(1, 2):
    # URL da página desejada
    url_vimeo = f"https://vimeo.com/search/page:{page}/sort:latest?duration=long&q=aula"
    
    # Abrir a página desejada
    time.sleep(10)
    driver.get(url_vimeo)
    
    # Aguardar alguns segundos para carregar todo o conteúdo da página
    time.sleep(10)

    # Scroll to the bottom of the page using ActionChains
    while True:
        try:
            # Find all <a> elements with class "iris_video-vital__overlay"
            videos = driver.find_elements(By.CSS_SELECTOR, "a.iris_video-vital__overlay")

            # Store the links of the found videos
            video_links = []
            for video in videos:
                video_links.append(video.get_attribute("href"))

            # Find all <span> elements with class "iris_link iris_link--gray-2"
            video_titles = driver.find_elements(By.CSS_SELECTOR, "span.iris_link.iris_link--gray-2")

            # Store the titles of the found videos
            video_titles_list = []
            for title in video_titles:
                video_titles_list.append(title.get_attribute("title"))

            # Dictionary with links and titles of the videos
            video_dict = dict(zip(video_links, video_titles_list))
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
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

time.sleep(5)

# Get the playlist and write to file
try:
    with open('./VIMEOPLAY1.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
        for i, link in enumerate(links):
            # Get the stream information using streamlink
            streams = streamlink.streams(link)
            url = streams['best'].url
            # Write the stream information to the file
            title = titles[i]

            f.write(f"#EXTINF:-1 group-title=\"VIMEO1\",{title}\n")
            f.write(f"{url}\n\n")
            f.write("\n")            
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")
    
    

