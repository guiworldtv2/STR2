import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

search_terms = ["bbvip", "big brother"]

m3u8_file = open("lista_twitches.m3u8", "w")

for search_term in search_terms:
    search_url = f"https://www.twitch.tv/search?term={search_term}"

    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    channels = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv tw-link")

    for channel in channels:
        channel_url = "https://www.twitch.tv" + channel["href"]
        channel_name = channel.text
        
        m3u8_file.write(f"#EXTINF:-1,{channel_name}\n{channel_url}\n\n")

m3u8_file.close()
