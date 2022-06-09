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
#EXTINF:-1,El Trece Internacional
http://live.budtvlight.com:25461/live/JW2WBKKNRE3UH43KN2N322899665975$5234/MENR32222XAAASA1XAAASA1/1815.m3u8
#EXTINF:-1,C5N
http://45.238.54.70:8000/play/a01e
#EXTINF:-1,Crðnica
http://45.238.54.70:8000/play/a01f
#EXTINF:-1,Encuentro
http://45.238.54.70:8000/play/a01b
#EXTINF:-1, tvg-id="Telefe" group-title="Argentina" tvg-name="Telefe" tvg-logo="http://www.lanoticiawebciudad.com.ar/wp-content/uploads/2016/11/telefe-logo.jpg",Telefe
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/TelefeHD/SA_SAGEMCOM/TelefeHD.m3u8
#EXTINF:-1,TELEFE
http://live.budtvlight.com:25461/live/JW2WBKKNRE3UH43KN2N322899665975$5234/MENR32222XAAASA1XAAASA1/1793.m3u8
#EXTINF:-1,Telefe Internacional
http://45.238.54.70:8000/play/a00b
#EXTINF: -1 tvg-logo="https://i.imgur.com/HvCzSJQ.png", TeleFe Rosario | HD | Argentina
https://m3u-editor.com/serve/televitolibre/497955335.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",América TV
https://edge2-ccast-sl.cvattv.com.ar/live/c3eds/AmericaTV/SA_SAGEMCOM/AmericaTV.m3u8
#EXTINF:-1  tvg-id="N/A" group-title="Argentina" tvg-logo="N/A",IP - Información Periodística
https://octubre-live.cdn.vustreams.com/live/ip/live.isml/live-audio_1=128000-video=2800000.m3u8


#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/37/Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg/260px-Informaci%C3%B3n_Period%C3%ADstica_IP_Logo.svg.png" group-title="NOTICIAS", IP  24.5         
https://d1nmqgphjn0y4.cloudfront.net/live/ip/live.isml/live-audio_1=128000-video=4499968.m3u8

#EXTINF:-1 tvg-logo="http://www.grupocronica.com.ar/mediakit/wp-content/uploads/2017/10/cronica-hd-con-sombra-grande.png" group-title="NOTICIAS", CRONICA HD  24.4
https://g5.vxral-slo.transport.edge-access.net/b10/ngrp:cronicatv_video1-100044_all/cronicatv_video1-100044_720p/index.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/LogoCanal26.png/120px-LogoCanal26.png" group-title="NOTICIAS", CANAL 26  24.2
http://live-edge01.telecentro.net.ar/live/smil:c26.smil/chunklist_w794690609_b2628000_sleng.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/82/A24_%282019-1%29.png/150px-A24_%282019-1%29.png" group-title="NOTICIAS", A24  36.3
https://g1.vxral-hor.transport.edge-access.net/a15/ngrp:a24-100056_all/a24-100056_720p.m3u8

#EXTINF:-1 group-title="NOTICIAS", TODO NOTICIAS       
https://www.youtube.com/watch?v=wHn1_QVoXGM

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/c/c8/Am%C3%A9rica_TV_%28Nuevo_logo_Junio_2020%29.png" group-title="AMBA", AMERICA HD  36.1
https://prepublish.f.qaotic.net/a07/americahls-100056/playlist_720p.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/b/b0/Canal9.jpg" group-title="AMBA", CANAL 9  35.1 
https://ar-elnueve-elnueve-live.ned.media/live.m3u8?iut=eyJwYXJhbXMiOnsiZXhwIjoxNjI5NDY0OTI5LCJzZXNzaW9uIjoiMTgxLjQ0LjEyOS43MSIsIndoaXRlbGlzdCI6WyIxODEuNDQuMTI5LjcxIl19LCJzaWduYXR1cmUiOiJjNzQ2NTZjMjM0MjI5MmYwMDBhMzExZjNlYWIzMzBlNzVmYjJmNzY1In0=

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/c/cc/Telefe_%28nuevo_logo%29.png/800px-Telefe_%28nuevo_logo%29.png" group-title="AMBA", TELEFE  34.1
https://telefe.com/Api/Videos/GetSourceUrl/694564/0/HLS?.m3u8

#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5f523aa5523ae000074745ec/colorLogoPNG.png" group-title="NOTICIAS", TELEFÉ NOTICIAS
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5f523aa5523ae000074745ec/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff334c2-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=dffc36b9-57c6-4973-9903-2f83d465ac40&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/8f/Canal13_logo.png" group-title="AMBA", CANAL 13  33.1
http://edge5-sl.cvattv.com.ar/live/c3eds/ArtearHD/SA_SAGEMCOM/ArtearHD-avc1_379968=10016.m3u8



#EXTINF:-1 tvg-logo="https://scontent.fepa11-1.fna.fbcdn.net/v/t1.6435-9/206638151_10223169123710059_3666810289391430657_n.jpg?_nc_cat=101&ccb=1-3&_nc_sid=825194&_nc_eui2=AeGxugJ54qa7RhgKBnLTrHOu14OonvQq8lrXg6ie9CryWkCQzaYyrufVmZGkiprZVM0&_nc_ohc=dbLCQPiMFxEAX9X0jrT&_nc_ht=scontent.fepa11-1.fna&oh=afeef92e5377cb7720df7b2f4afc60c8&oe=6127F95F" group-title="AMBA", SSIPTV ARG TV
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5df265697ec3510009df1ef0/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1d530-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=ec2383fd-6e28-4df5-9d1c-b66eee700e0c&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Net_TV_logo.png/120px-Net_TV_logo.png" group-title="AMBA", NET TV  27.2
https://unlimited1-us.dps.live/nettv/nettv.smil/nettv/livestream1/playlist.m3u8

#EXTINF:-1 tvg-logo="https://pbs.twimg.com/profile_images/1088570060887810048/IAlLnIgQ.jpg" group-title="AMBA", CANAL DE LA CIUDAD
https://g2.proy-slo.transport.edge-access.net/a08/ngrp:gcba_video4-100042_all/gcba_video4-100042_540p.m3u8               

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Logo_del_canal_Encuentro.svg/150px-Logo_del_canal_Encuentro.svg.png" group-title="AMBA", CANAL ENCUENTRO 22.1
https://5fb24b460df87.streamlock.net/live-cont.ar/encuentro/playlist.m3u8  

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/2/2a/Paka-paka.svg/245px-Paka-paka.svg.png" group-title="AMBA", PAKA PAKA  22.2
https://5fb24b460df87.streamlock.net/live-cont.ar/pakapaka/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Logo_The_Simpsons.svg/1200px-Logo_The_Simpsons.svg.png" group-title="AMBA", LOS SIMPSONS
https://videostreaming.cloudserverlatam.com/cloudservertv/cloudservertv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/d/d6/Logomagic96.png" group-title="AMBA", MAGIC KIDS
https://live.admefy.com/live/clean_peach_ef224.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/38/Cine.Ar_logo.svg/1280px-Cine.Ar_logo.svg.png" group-title="AMBA", CINEAR  22.4
https://5fb24b460df87.streamlock.net/live-cont.ar/cinear/playlist.m3u8   

#EXTINF:-1 tvg-logo="http://images.pluto.tv/channels/5de91cf02fc07c0009910465/colorLogoPNG.png" group-title="AMBA", TELEFÉ CLÁSICO
http://service-stitcher.clusters.pluto.tv/stitch/hls/channel/5de91cf02fc07c0009910465/master.m3u8?advertisingId=&appName=web&appVersion=unknown&appStoreUrl=&architecture=&buildVersion=&clientTime=0&deviceDNT=0&deviceId=bff1ae23-6307-11eb-b3fa-019cb96f121b&deviceMake=Chrome&deviceModel=web&deviceType=web&deviceVersion=unknown&includeExtendedEvents=false&sid=a367d0d9-b23d-4bb5-8d48-55f0cbeac4fb&userId=&serverSideAds=true

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/gwVNQhVICXN4Q7djaLyeQGCiMAa4Jum_PqeVaFZ1W90T4Y0G297wC1upnHRcKUbA6Q=w412-h220-rw" group-title="AMBA", GEN TV  17.3
https://videohd.live:19360/8010/8010.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-Od4eldPqILM/XjtCKHxeYSI/AAAAAAAAvok/HDnuaXs9cCsFzbr0QrQtw3bYeDB0_5osACK8BGAsYHg/s0/2020-02-05.png" group-title="AMBA", CINCO TV TIGRE  30.1
https://59537faa0729a.streamlock.net/cincotv/cincotv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://neotvdigital.com.ar/imagenes/logo1.png" group-title="AMBA", NEO TV DIGITAL  14.1
https://videostream.shockmedia.com.ar:19360/neotvdigital/neotvdigital.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMm0MM0BtkhB9xHWsECtnky05aGfA8KKnDSg&usqp=CAU" group-title="AMBA", CANAL 29 QUILMES 18.1
http://inliveserver.com:1935/8386/8386/playlist.m3u8

#EXTINF:-1 tvg-logo="https://serenotv.com/wp-content/uploads/2020/08/canal-telecreativa.jpg" group-title="AMBA", TELECREATIVA LANUS
https://panel.dattalive.com/8012/8012/playlist.m3u8

#EXTINF:-1 tvg-logo="https://image.winudf.com/v2/image1/Y29tLmExMjNmcmVlYXBwcy5mcmVlLmFwcDVkNWVjMWY4ODliOThfaWNvbl8xNTY3NjE5OTcxXzAxNw/icon.png?w=170&fakeurl=1" group-title="AMBA", CANAL 4 TELEAIRE SAN MARTIN
https://stmvideo2.livecastv.com/canal4/canal4/playlist.m3u8

#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-SlqJrd0GiYk/XjtCBz2FbhI/AAAAAAAAvog/HkkKzNWrEOYiE08Rdlw-mxsDtzpJ_zD8wCK8BGAsYHg/s0/2020-02-05.png" group-title="AMBA", CANAL 6 MORENO
https://5975e06a1f292.streamlock.net:4443/canal6moreno/canal6moreno/playlist.m3u8

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VIC2PROV.png" group-title="AMBA", PROVINCIAL TV
http://www.trimi.com.ar/provincial/streaming/mystreamProvincialHSMed.m3u8

#EXTINF:-1 tvg-logo="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRG3riJIJamJMTaIwOIMuqH2cdOfdLQIyz9-NHeJ-pF2tQJsM-akUEu5MuYVspASJxZNQ&usqp=CAU" group-title="AMBA", CIUDAD MAGAZINE
https://g4.mc-slo.transport.edge-access.net/a09/ngrp:magazine_live01-100083_all/magazine_live01-100083_720p.m3u8

#EXTINF:-1 tvg-logo="http://www.canalkzo.com/images/lg_kzo.svg" group-title="AMBA", KZO
http://g2.vxral-slo.transport.edge-access.net/nx-beta/nx.hor.livetx.01/5eaa642772b3a25e2c28699e_540p/index.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/8/87/DeporTV_%282020_Logo_oficial%29.png" group-title="AMBA", DEPORT TV 24.1
https://5fb24b460df87.streamlock.net/live-cont.ar/deportv/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/TYC_SPORTS.jpg/800px-TYC_SPORTS.jpg" group-title="AMBA", TyC SPORT 
https://d3055hobuue3je.cloudfront.net/out/v1/b841c366cbe540e6a106c3ba83e5c8d6/index.m3u8

#EXTINF:-1 tvg-logo="https://i.ibb.co/NTNvh66/header-ciudadmagica.jpg" group-title="DEPORTE", CIUDAD MAGICA TV
https://srv2.zcast.com.br/ciudadm/ciudadm/playlist.m3u8



#EXTINF:-1 tvg-logo="https://lh3.googleusercontent.com/-2gN4wEv_qPI/XjtKDwMuIQI/AAAAAAAAvrY/VTtJwZALBykDRnM8ia0Xbqi0FbREvdrZACK8BGAsYHg/s0/2020-02-05.png" group-title="AMBA", GARAGE TV
http://186.0.233.76:1935/Garage/smil:garage.smil/chunklist_w2049053275_b1296000_sleng.m3u8

#EXTINF:-1 tvg-logo="https://cdn-profiles.tunein.com/s303640/images/logog.png?t=151602" group-title="NOTICIAS", FRANCE 24 ESPAÑOL - 24.3
http://f24hls-i.akamaihd.net/hls/live/520845/F24_ES_HI_HLS/master.m3u8

#EXTINF:-1 tvg-logo="https://www.telesurtv.net/export/sites/telesur/arte/log-iso-telesur.png_253617125.png" group-title="NOTICIAS", TELESUR  25.4
https://d2ajt1gpdtnw25.cloudfront.net/mbliveMain/480p/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a0/Russia-today-logo.svg/1200px-Russia-today-logo.svg.png" group-title="NOTICIAS", RT  25.5
https://rt-esp-gd.secure2.footprint.net/1102.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/3/39/Euronews._2016_alternative_logo.png/600px-Euronews._2016_alternative_logo.png" group-title="NOTICIAS", EURONEWS
https://euronews-euronews-spanish-2.plex.wurl.com/manifest/playlist.m3u8

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/7/75/Deutsche_Welle_symbol_2012.svg/150px-Deutsche_Welle_symbol_2012.svg.png" group-title="NOTICIAS", DW ESPAÑOL
https://dwamdstream104.akamaized.net/hls/live/2015530/dwstream104/stream05/streamPlaylist.m3u8

#EXTINF:-1 tvg-logo="http://tvabierta.weebly.com/uploads/5/1/3/4/51344345/mirador.png" group-title="AMBA", MIRADOR  22.3
https://5fb24b460df87.streamlock.net/live-cont.ar/mirador/playlist.m3u8 

#EXTINF:-1 tvg-logo="https://upload.wikimedia.org/wikipedia/commons/4/4c/Telemax.png" group-title="AMBA", TELEMAX  26.3
https://live-edge01.telecentro.net.ar/live/smil:tlx.smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://d2ucqd3jt48qxz.cloudfront.net/img/footer-logo.png" group-title="AMBA", ORBE 21  21.2
https://cdn2.zencast.tv:30443/orbe/orbe21smil/playlist.m3u8

#EXTINF:-1 tvg-logo="https://dz92jh1unkapm.cloudfront.net/accounts/5cf95117cb97cae8e2c36676/logo.png" group-title="AMBA", UNIFE TV  25.1
https://dcunilive262-lh.akamaihd.net/i/dclive_1@424583/index_150_av-b.m3u8?sd=10&rebase=on

#EXTINF:-1 tvg-logo="http://www.radiosargentina.com.ar/png/VISANTAM.png" group-title="AMBA", SANTA MARIA
http://www.trimi.com.ar/santa_maria/streaming/mystreamSantaMariaHSMed.m3u8



#EXTINF:-1 tvg-logo="http://www.tectv.gob.ar/resources/img/logo.png" group-title="AMBA", TEC TV  22.5
https://g3.mc-hor.transport.edge-access.net/a09/ngrp:gcba_video3-100042_all/gcba_video3-100042_720p.m3u8





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
