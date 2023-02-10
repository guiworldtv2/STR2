import requests
import time
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}

url = "https://www.twitch.tv/search?term=bbvip"

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

links = []

for link in soup.find_all("a", {"class": "ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link"}):
    links.append("https://www.twitch.tv" + link["href"])

time.sleep(10)

with open("BBVIPALBANIA.txt", "w") as file:
    for link in links:
        file.write(link + "\n")
