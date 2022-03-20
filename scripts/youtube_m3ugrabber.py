#! /usr/bin/python3

banner = r'''
###########################################################################
#                                                                         #

#                                  >> https://github.com/guiworldtv       #
###########################################################################

#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",MTV LATINOAMERICA
https://edge2-ccast-sl.cvattv.com.ar/live/c6eds/MTV_HD/SA_SAGEMCOM/MTV_HD.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El Trece
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",El Trece 2
https://live-01-02-eltrece.vodgc.net/eltrecetv/tracks-v1a1/mono.m3u8
#EXTINF:-1,el trece Internacional
http://45.238.54.70:8000/play/a00a
#EXTINF:-1,C5N
http://45.238.54.70:8000/play/a01e
#EXTINF:-1,Crðnica
http://45.238.54.70:8000/play/a01f
#EXTINF:-1,Encuentro
http://45.238.54.70:8000/play/a01b
#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="http://www.lanoticiawebciudad.com.ar/wp-content/uploads/2016/11/telefe-logo.jpg",Telefe
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/TelefeHD/SA_SAGEMCOM/TelefeHD.m3u8
#EXTINF:-1,Telefe Internacional
http://45.238.54.70:8000/play/a00b
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",América TV
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/AmericaTV/SA_SAGEMCOM/AmericaTV.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",IP - Información Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8
#EXTINF:-1, CANAL 26 
http://200.115.193.177/live/26hd-720/.m3u8

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
                print('https://vimeo.com/172452956')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://vimeo.com/172452956')
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

print('#EXTM3U x-tvg-url="https://iptv-org.github.io/epg/guides/ar/mi.tv.epg.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/mudstein/XML/main/TIZENsiptv.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/K-vanc/Tempest-EPG-Generator/main/Siteconfigs/Argentina/%5BENC%5D%5BEX%5Delcuatro.com_0.channel.xml"')
print('#EXTM3U x-tvg-url="https://raw.githubusercontent.com/Nicolas0919/Guia-EPG/master/GuiaEPG.xml"')
print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt', errors="ignore") as f:
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
