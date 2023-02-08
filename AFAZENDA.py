import requests
from bs4 import BeautifulSoup
import datetime
import streamlink

import re




headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}

m3u8_file = open("AFAZENDA.m3u8", "w")

for i in range(1, 3):
    url = f"https://tviplayer.iol.pt/videos/ultimos/{i}/canal:"

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    video_titles = [item.text for item in soup.find_all("span", class_="item-title")]
    video_links = [f"https://tviplayer.iol.pt{item['href']}" for item in soup.find_all("a", class_="item")]
    Data = [item.text for item in soup.find_all("span", class_="item-date")]

    for title, link, data in zip(video_titles, video_links, Data):
        if data == "Hoje":
            date_object = datetime.datetime.now()
        elif data == "Ontem":
            date_object = datetime.datetime.now() - datetime.timedelta(days=1)
        else:
            date_object = datetime.datetime.strptime(data, '%d %b %Y')
        timestamp = date_object.strftime("%m%d")
        video_url = streamlink.streams(link)["best"].url
        m3u8_file.write(f"#EXTINF:-1,{timestamp}_SBTVD_{title}_-ANO\n{video_url}\n")
        
        
    def format_date(data):
    data = re.sub("(seg|ter|qua|qui|sex|sab|dom)", "", data)
    data = data.strip()
    if len(data) == 1:
        data = "0" + data
    return data

data = "Seg, 6 fev 2023"
data = format_date(data)
print(data)






m3u8_file.close()


