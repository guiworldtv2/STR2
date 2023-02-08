import streamlink
import subprocess

# Install streamlink
subprocess.run(["pip", "install", "--user", "--upgrade", "streamlink"])

# Get LISTA4.m3u8
with open("./BBVIPALBANIA.m3u8", "w") as f:
    f.write("#EXTM3U\n")
    f.write("#EXT-X-VERSION:3\n")
    f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")
    

    with open("BBVIPALBANIA.txt") as txt_file:
        for line in txt_file:
            # Get the Twitch URL from each line in BBVIPALBANIA2.txt
            twitch_url = line.strip()

            # Run streamlink and get the stream URL
            stream_url = subprocess.run(["streamlink", "--url", "--default-stream", "--stream-url", twitch_url, "best"], capture_output=True, text=True).stdout.strip()

            f.write(stream_url + "\n")

            
