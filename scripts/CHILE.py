#! /usr/bin/python3

banner = r'''
###########################################################################
#                                                                         #

#                                  >> https://github.com/guiworldtv       #
###########################################################################

#EXTINF:-1,TVN
https://marine2.miplay.cl/tvn/mono.m3u8
#EXTINF:-1,CHV
https://marine2.miplay.cl/chilevision/index.m3u8
#EXTINF:-1,Chile: Chilevision
http://goldiptv.online:8080/mevlut/mevlut123/27111
#EXTINF:-1,Chile: Chilevision HD
http://goldiptv.online:8080/mevlut/mevlut123/27110
#EXTINF:-1,Chile: CNN HD
http://goldiptv.online:8080/mevlut/mevlut123/27109
#EXTINF:-1,052 24 HORAS
http://45.181.121.57:8111/play/052
#EXTINF:-1,054 CNN Chile
http://45.181.121.57:8111/play/054
#EXTINF:-1,062 La Red HD
http://45.181.121.57:8111/play/062
#EXTINF:-1,064 TVN HD
http://45.181.121.57:8111/play/064
#EXTINF:-1,065 Mega
http://45.181.121.57:8111/play/065
#EXTINF:-1,065 Mega SD
https://unlimited1-cl-isp.dps.live/mega/mega.smil/playlist.m3u8
#EXTINF:-1,066 CHV HD
http://45.181.121.57:8111/play/066
#EXTINF:-1,067 Canal 13
http://45.181.121.57:8111/play/067
#EXTINF:-1,Chile: 13C HD
http://goldiptv.online:8080/mevlut/mevlut123/27120
#EXTINF:-1,Chile: 13i HD
http://goldiptv.online:8080/mevlut/mevlut123/27119
#EXTINF:-1,Chile: 24 Horas
http://goldiptv.online:8080/mevlut/mevlut123/27118
#EXTINF:-1,Chile: Canal 13 HD
http://goldiptv.online:8080/mevlut/mevlut123/27117
#EXTINF:-1,CHVNOTICIAS_PLUTOTV
https://siloh-latam-aka.plutotv.net/lilo/production/Chilevision/master.m3u8

'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/guiworldtv/MEU-IPTV-FULL/main/VideoOFFAir.m3u8')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/mi.tv.epg.xmll"')
print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/cl/gatotv.com.epg.xml"')
print(banner)
#s = requests.Session()
with open('../CHILE.txt', errors="ignore") as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
            
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
    
    
