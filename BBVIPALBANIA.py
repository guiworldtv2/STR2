import streamlink

with open("BBVIPALBANIA.txt", "r") as f:
    links = f.readlines()

for link in links:
    session = streamlink.Streamlink()
    session.set_option("twitch-disable-ads", True)
    session.set_option("twitch-disable-reruns", True)
    
    video_url = session.streams(link.strip())["best"].url if session.streams(link.strip()) else None

    if video_url:
        with open("BBVIPALBANIA.m3u8", "w") as m3u8_file:
            m3u8_file.write("#EXTM3U\n")
            m3u8_file.write("#EXT-X-VERSION:3\n")
            m3u8_file.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")
            m3u8_file.write(video_url + "\n")

    session.close()
