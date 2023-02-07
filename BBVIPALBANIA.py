import streamlink

session = streamlink.Streamlink()
session.set_option("twitch-disable-ads", True)
session.set_option("twitch-disable-reruns", True)

with open("BBVIPALBANIA.txt") as links_file:
    for link in links_file:
        link = link.strip()
        video_url = session.streams(link)["best"].url if session.streams(link) else None
        if video_url:
            m3u8_file = open(f"{link}.m3u8", "w")
            m3u8_file.write("#EXTM3U\n")
            m3u8_file.write("#EXT-X-VERSION:3\n")
            m3u8_file.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")
            m3u8_file.write(video_url + "\n")
            m3u8_file.close()

session.close()

