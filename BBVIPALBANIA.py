import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("BBVIPALBANIA.m3u8", "w")

for search_term in ["bbvip", "big%20brother"]:
    url = f"https://www.twitch.tv/search?term={search_term}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    stream_links = [f"https://www.twitch.tv{item['href']}" for item in soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv tw-link")]

    for link in stream_links:
        video_url = link
        m3u8_file.write(f"#EXTINF:-1 group-title=\"TWITCH\",{link}\n{video_url}\n")
        m3u8_file.write("\n")

m3u8_file.close()

