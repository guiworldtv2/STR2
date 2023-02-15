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

# Scroll to the bottom of the page using ActionChains
while True:
    try:
        for page in range(1, 12):
        # URL da página desejada
        url_vimeo = f"https://vimeo.com/search/page:{page}/sort:latest?duration=long&q=aula"

        # Abrir a página desejada
        driver.get(url_vimeo)

        # Aguardar alguns segundos para carregar todo o conteúdo da página
        time.sleep(5)

        # Find all <a> elements with class "js-preview-link"
        videos_found = driver.find_elements(By.CSS_SELECTOR, "a.js-preview-link")

        # Store the links of the found videos
        video_links = []
        for video in videos_found:
            video_links.append(video.get_attribute("href"))

        # Find all <h3> elements with class "preview__title"
        video_titles = driver.find_elements(By.CSS_SELECTOR, "h3.preview__title")

        # Store the titles of the found videos
        video_titles_list = []
        for title in video_titles:
            video_titles_list.append(title.text)

        # Dictionary with links and titles of the videos
        video_dict = dict(zip(video_links, video_titles_list))
        
        # If no more videos are found, break the loop
        if len(videos_found) == 0:
            break

        # Scroll down to load more videos
        actions = ActionChains(driver)
        actions.move_to_element(videos_found[-1])
        actions.perform()

        time.sleep(5)
    except:
        break
        
        
# Get the page source again after scrolling to the bottom
html_content = driver.page_source

time.sleep(5)

try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", class_="iris_video-vital__overlay")
    links = [video.get("href") for video in videos]
    titles = [video.get("title") for video in videos]
    print("Links dos vídeos encontrados:")
    print(links)
    print("Títulos dos vídeos encontrados:")
    print(titles)
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
