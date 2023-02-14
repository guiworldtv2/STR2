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

# Obter o conteúdo da página com BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

with open('twitch_clips.m3u', 'w') as f:
    clips = soup.find_all('div', {'class': 'clip-card'})
    for clip in reversed(clips):
        videos = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link", href=True)
        channels = soup.find_all("p", class_="ScCoreParagraph-sc-1ein8td-0 iJknhp tw-ellipsis", title=True)
        thumbnails = soup.find_all("img", class_="tw-image")
        links = ["https://www.twitch.tv" + video.get("href") for video in videos]
        titles = [video.find("h3").get("title") for video in videos]
        channel_names = [channel.get("title") for channel in channels]
        thumbnail_links = [thumbnail.get("src") for thumbnail in thumbnails]

        for i in range(len(links)):
            print(f"Title: {titles[i]}")
            print(f"Channel: {channel_names[i]}")
            print(f"Thumbnail: {thumbnail_links[i]}")
            print(f"Link: {links[i]}\n")


        f.write(f'#EXTINF:-1 tvg-logo="{thumbnail}" group-title="{channel}",{title}\n{video_link}\n')
