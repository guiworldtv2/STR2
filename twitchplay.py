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

# Criar objeto BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

with open('twitch_clips.m3u', 'w') as f:
    clips = soup.find_all('div', {'class': 'clip-card'})
    for clip in reversed(clips):
        title = clip.find('h3', {'class': 'CoreText-sc-1txzju1-0 eJuFGD'})['title']
        channel = clip.find('p', {'data-a-target': 'preview-card-channel-link'}).text
        thumbnail = clip.find('img', {'class': 'tw-image'})['src']
        video_link = 'https://www.twitch.tv' + clip.find('a', {'data-a-target': 'preview-card-image-link'})['href']

        f.write(f'#EXTINF:-1 tvg-logo="{thumbnail}" group-title="{channel}",{title}\n{video_link}\n')
