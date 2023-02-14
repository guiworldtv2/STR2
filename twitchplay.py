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

# Find the links and titles of the first four videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link", href=True)
    links = ["https://www.twitch.tv" + video.get("href") for video in videos]
    titles = [video.find("h3").get("title") for video in videos]

    # Print the titles and links of the first four videos in reverse order
    for i in range(len(links)):
        print("Titulo:", titles[i])
        print("Link:", links[i], "\n")
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()

