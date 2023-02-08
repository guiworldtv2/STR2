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
            result = subprocess.run(["streamlink", "--url", "--default-stream", "--stream-url", twitch_url, "best"], capture_output=True, text=True)

            if result.returncode == 0:
                stream_url = result.stdout.strip()
                f.write(stream_url + "\n")
            else:
                f.write("https://raw.githubusercontent.com/guiworldtv/STR2/main/VideoOFFAir.m3u8\n")
