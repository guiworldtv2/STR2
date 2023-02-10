import requests
from bs4 import BeautifulSoup
import time

url = "https://www.twitch.tv/search?term=bbvip"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

response = requests.get(url, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

links = []
for link in soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link"):
    links.append(link["href"])

formatted_links = []
for link in links:
    formatted_links.append("https://www.twitch.tv" + link)

time.sleep(10)

# Get the wakerttv link
wakerttv_link = None
for link in soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 eYjhIv tw-link"):
    if link["href"] == "/wakerttv":
        wakerttv_link = "https://www.twitch.tv" + link["href"]
        break

if wakerttv_link:
    formatted_links.append(wakerttv_link)

with open("BBVIPALBANIA.txt", "w") as f:
    for link in formatted_links:
        f.write(link + "\n")
