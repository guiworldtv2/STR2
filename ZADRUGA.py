from __future__ import unicode_literals
import requests
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup
from pytube import YouTube

channel_no = 0
m3u = None

def get_video_info(video_url):
    try:
        yt = YouTube(video_url)
        return {
            "url": video_url,
            "title": yt.title,
            "image": yt.thumbnail_url,
            "description": yt.description
        }
    except Exception as e:
        return None

banner = '''#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000
'''

def generate_youtube_playlist():
    global channel_no, m3u
    m3u = open("ZADRUGA_playlist.m3u8", "w")
    m3u.write(banner)

    with open('ZADRUGA.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            channel = get_video_info(line)
            if channel is None:
                continue
            try:
                video = get_video_info(line)
                if video is None:
                    continue
                video_link = video['url']
                channel_no += 1
                channel_name = f"{channel_no}-{line.split('/')[-1]}"
                playlistInfo = f"#EXTINF:-1 tvg-chno=\"{channel_no}\" tvg-id=\"{line}\" tvg-name=\"{channel_name}\" tvg-logo=\"{channel.get('image')}\" group-title=\"ZADRUGA\",{channel.get('title')}\n"                
                m3u.write(playlistInfo)
                m3u.write(video_link)
                m3u.write("\n")
            except Exception as e:
                print(e)

    m3u.close()

if __name__ == '__main__':
    generate_youtube_playlist()
