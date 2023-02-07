import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

search_terms = ['bbvip', 'big%20brother']

m3u8_file = open("BBVIPALBANIA.m3u8", "w")
m3u8_file.write("#EXTM3U\n")
m3u8_file.write("#EXT-X-VERSION:3\n")
m3u8_file.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")

for term in search_terms:
    url = f"https://www.twitch.tv/search?term={term}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    channel_links = [f"https://www.twitch.tv{item['href']}" for item in soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv tw-link")]

    for link in channel_links:
        video_url = streamlink.streams(link)["best"].url if streamlink.streams(link) else None
        if video_url:
            m3u8_file.write(f"{video_url}\n")

m3u8_file.close()
