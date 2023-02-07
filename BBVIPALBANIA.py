import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("lista2str2.m3u", "w")

search_terms = ["bbvip", "big%20brother"]

for search_term in search_terms:
    url = f"https://www.twitch.tv/search?term={search_term}"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    stream_links = [f"https://www.twitch.tv{item['href']}" for item in soup.find_all("a", class_="tw-link")]

    for link in stream_links:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        try:
            stream_url = soup.find("source")["src"]
        except TypeError:
            continue

        m3u8_file.write(f"#EXTINF:-1 group-title=\"TWITCH\",{link}\n{stream_url}\n")
        m3u8_file.write("\n")

m3u8_file.close()
