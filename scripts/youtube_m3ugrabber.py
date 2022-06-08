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
#EXTINF: -1 tvg-logo="https://i.imgur.com/HvCzSJQ.png", TeleFe Rosario | HD | Argentina
https://m3u-editor.com/serve/televitolibre/497955335.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",América TV
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/AmericaTV/SA_SAGEMCOM/AmericaTV.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",IP - Información Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8
#EXTINF:-1, CANAL 26 
http://200.115.193.177/live/26hd-720/.m3u8
#EXTINF:-1, A24 FHD*
http://goldiptv.online:8080/mevlut/mevlut123/27183
#EXTINF:-1, A24 HD*
http://goldiptv.online:8080/mevlut/mevlut123/27182
#EXTINF:-1, America TV FHD*
http://goldiptv.online:8080/mevlut/mevlut123/27180
#EXTINF:-1, America TV HD
http://goldiptv.online:8080/mevlut/mevlut123/27179
#EXTINF:-1, C5N HD*
http://goldiptv.online:8080/mevlut/mevlut123/27178
#EXTINF:-1, Canal 26 Noticias HD*
http://goldiptv.online:8080/mevlut/mevlut123/27177
#EXTINF:-1, Canal 4 Esquel
http://goldiptv.online:8080/mevlut/mevlut123/27176
#EXTINF:-1, Canal 9 Salta
http://goldiptv.online:8080/mevlut/mevlut123/27175
#EXTINF:-1, CINE.AR HD*
http://goldiptv.online:8080/mevlut/mevlut123/27174
#EXTINF:-1, CN23 HD*
http://goldiptv.online:8080/mevlut/mevlut123/27173
#EXTINF:-1, Cronica Television HD*
http://goldiptv.online:8080/mevlut/mevlut123/27172
#EXTINF:-1, DeporTV FHD*
http://goldiptv.online:8080/mevlut/mevlut123/27171
#EXTINF:-1, DeporTV HD*
http://goldiptv.online:8080/mevlut/mevlut123/27170
#EXTINF:-1, El Garage TV HD
http://goldiptv.online:8080/mevlut/mevlut123/27169
#EXTINF:-1, El Nueve FHD*
http://goldiptv.online:8080/mevlut/mevlut123/27168
#EXTINF:-1, El Nueve HD*
http://goldiptv.online:8080/mevlut/mevlut123/27167
#EXTINF:-1, El Rural HD*
http://goldiptv.online:8080/mevlut/mevlut123/27166
#EXTINF:-1, El trece FHD*
http://goldiptv.online:8080/mevlut/mevlut123/27165
#EXTINF:-1, El trece HD*
http://goldiptv.online:8080/mevlut/mevlut123/27164
#EXTINF:-1, Fox Sports 1
http://goldiptv.online:8080/mevlut/mevlut123/27162
#EXTINF:-1, Fox Sports 2
http://goldiptv.online:8080/mevlut/mevlut123/27161
#EXTINF:-1, Fox Sports Premium FHD
http://goldiptv.online:8080/mevlut/mevlut123/27160
#EXTINF:-1, Fox Sports Premium HD
http://goldiptv.online:8080/mevlut/mevlut123/27159
#EXTINF:-1, LN Mas HD*
http://goldiptv.online:8080/mevlut/mevlut123/27158
#EXTINF:-1, Net TV FHD
http://goldiptv.online:8080/mevlut/mevlut123/27157
#EXTINF:-1, Net TV HD
http://goldiptv.online:8080/mevlut/mevlut123/27156
#EXTINF:-1, Telefe FHD*
http://goldiptv.online:8080/mevlut/mevlut123/27152
#EXTINF:-1, Telefe HD*
http://goldiptv.online:8080/mevlut/mevlut123/27151
#EXTINF:-1, Telemax
http://goldiptv.online:8080/mevlut/mevlut123/27150
#EXTINF:-1, Television Publica FHD*
http://goldiptv.online:8080/mevlut/mevlut123/27149
#EXTINF:-1, Television Publica HD*
http://goldiptv.online:8080/mevlut/mevlut123/27148
#EXTINF:-1, TN Buenos Aires
http://goldiptv.online:8080/mevlut/mevlut123/27147
#EXTINF:-1, TNT Sports HD
http://goldiptv.online:8080/mevlut/mevlut123/27146
#EXTINF:-1, TR Telered
http://goldiptv.online:8080/mevlut/mevlut123/27145
#EXTINF:-1, Trece Max HD
http://goldiptv.online:8080/mevlut/mevlut123/27144
#EXTINF:-1, TyC Sports FHD
http://goldiptv.online:8080/mevlut/mevlut123/27143
#EXTINF:-1, TyC Sports HD
http://goldiptv.online:8080/mevlut/mevlut123/27142
#EXTINF:-1, TyC Sports Internacional
http://goldiptv.online:8080/mevlut/mevlut123/27141

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
                print('https://eu-nl-012.worldcast.tv/dancetelevisionone/2/dancetelevisionone.m3u8')
                return
            os.system(f'wget {url} -O temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://eu-nl-012.worldcast.tv/dancetelevisionone/2/dancetelevisionone.m3u8')
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
