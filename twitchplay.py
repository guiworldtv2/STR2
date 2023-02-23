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
url_twitch = "https://www.twitch.tv/directory/game/Just%20Chatting?sort=VIEWER_COUNT&tl=espa%C3%B1ol"

# Abrir a página desejada
driver.get(url_twitch)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Define o seletor CSS do elemento que contém a lista de itens
lista_css_selector = ".tw-tower > div"

# Espera até que o elemento da lista esteja presente e visível
elemento_lista = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CSS_SELECTOR, lista_css_selector))
)
WebDriverWait(driver, 10).until(
    EC.visibility_of(elemento_lista)
)

# Rola a página para baixo até o final da lista
ultimo_item_css_selector = f"{lista_css_selector}:last-child"
ultimo_item = driver.find_element(By.CSS_SELECTOR, ultimo_item_css_selector)
driver.execute_script("arguments[0].scrollIntoView();", ultimo_item)
        
# Get the page source again after scrolling to the bottom
html_content = driver.page_source

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link", href=True)
    links = ["https://www.twitch.tv" + video.get("href") for video in videos]
    channels = [video.find("p", {"data-a-target": "preview-card-channel-link", "class": "CoreText-sc-1txzju1-0 jiepBC"}).get("title") for video in videos]
    titles = [video.find("h3", class_="CoreText-sc-1txzju1-0 eJuFGD").get("title") for video in videos]
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
