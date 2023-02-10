import requests
from bs4 import BeautifulSoup
import time

url = "https://www.twitch.tv/search?term=bbvip"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36',
}

def get_links(url, headers):
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")
    links = []
    for link in soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link"):
        href = link.get("href")
        links.append(href)
    return links

def save_to_file(links):
    with open("BBVIPALBANIA.txt", "w") as f:
        for link in links:
            f.write("https://www.twitch.tv" + link + "\n")

if __name__ == "__main__":
    time.sleep(10)
    links = get_links(url, headers)
    save_to_file(links)
