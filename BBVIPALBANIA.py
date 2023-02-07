import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista_twitch.m3u", "w")

# url da twitch
urls = ["https://www.twitch.tv/search?term=bbvip", "https://www.twitch.tv/search?term=big%20brother"]

for url in urls:
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    # encontra todos os links da página
    video_links = [item["href"] for item in soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv tw-link")]
    
    # escreve cada link encontrado no arquivo
    for link in video_links:
        video_url = f"https://www.twitch.tv{link}"
        m3u8_file.write(video_url + "\n")

m3u8_file.close()
