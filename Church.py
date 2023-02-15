#! /usr/bin/python3

from __future__ import unicode_literals
import youtube_dl
import requests
import shutil
from urllib.request import urlopen
from bs4 import BeautifulSoup
channel_no = 0
m3u = None
def get_live_info(channel_id):
    try:
        webpage = urlopen(f"https://www.youtube.com/{channel_id}/live").read()
        soup = BeautifulSoup(webpage, 'html.parser')
        urlMeta = soup.find("meta", property="og:url")
        if urlMeta is None:
            return None
        url = urlMeta.get("content")
        if(url is None or url.find("/watch?v=") == -1):
            return None
        titleMeta = soup.find("meta", property="og:title")
        imageMeta = soup.find("meta", property="og:image")
        descriptionMeta = soup.find("meta", property="og:description")
        return {
            "url": url,
            "title": titleMeta.get("content"),
            "image": imageMeta.get("content"),
            "description": descriptionMeta.get("content")
        }
    
    except Exception as e:
                return None

banner = r'''
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000
'''

def generate_youtube_tv():
    global channel_no
    ydl_opts = {
        'format': 'best',
    }
    ydl = youtube_dl.YoutubeDL(ydl_opts)

    with open('Church.txt') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line == "":
                continue
            channel = get_live_info(line)
            if channel is None:
                continue
            try:
                with ydl:
                    result = ydl.extract_info(
                        f"https://www.youtube.com/{line}/live",
                        download=False  # We just want to extract the info
                    )

                    if 'entries' in result:
                        # Can be a playlist or a list of videos
                        video = result['entries'][-1]
                    else:
                        # Just a video
                        video = result
                video_url = video['url']

                channel_no += 1
                channel_name = f"{channel_no}-{line.split('/')[-1]}"
                playlistInfo = f"#EXTINF:-1 tvg-chno=\"{channel_no}\" tvg-id=\"{line}\" tvg-name=\"{channel_name}\" tvg-logo=\"{channel.get('image')}\" group-title=\"ARGENTINA\",{channel.get('title')}\n"                
                write_to_playlist(video_url)
                write_to_playlist("\n")
            except Exception as e:
                print(e)
                        



def write_to_playlist(content):
    global m3u    
    m3u.write(content)
    

def create_playlist():
    global m3u
    m3u = open("Church.m3u8", "w")
    m3u.write("#EXTM3U")
    m3u.write("\n")

    
def close_playlist():
    global m3u
    m3u.close()
def generate_youtube_PlayList():
    create_playlist()
        
    m3u.write(banner)

    generate_youtube_tv()
    

    

    


    close_playlist()


    
if __name__ == '__main__':
    generate_youtube_PlayList()   
