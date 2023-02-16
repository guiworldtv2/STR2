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

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Scroll to the bottom of the page by pressing "End" key for 1 minute
end_time = time.time() + 60  # 1 minute from now
while time.time() < end_time:
    driver.find_element_by_tag_name('body').send_keys(u'\ue010')
    time.sleep(1)

# Get the page source again after scrolling to the bottom
html_content = driver.page_source

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link", href=True)
    links = ["https://www.twitch.tv" + video.get("href") for video in videos][::-1]
    channels = [video.find("p", {"data-a-target": "preview-card-channel-link", "class": "CoreText-sc-1txzju1-0 jiepBC"}).get("title") for video in videos][::-1]
    titles = [video.find("h3", class_="CoreText-sc-1txzju1-0 eJuFGD").get("title") for video in videos][::-1]
    
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()

# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

# Get the playlist and write to file
try:
    with open('./TWITCHPLAY.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
        for i, link in enumerate(links):
            # Get the stream information using streamlink
            streams = streamlink.streams(link)
            url = streams['best'].url

            # Write the stream information to the file
            title = channels[i]

            f.write(f"#EXTINF:-1 tvg-id='{title}' tvg-logo=\"https://static-cdn.jtvnw.net/previews-ttv/live_user_{title}-1920x1080.jpg\" group-title=\"TWITCH\",{title}\n")            
            f.write(f"{url}\n")
            f.write("\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")

