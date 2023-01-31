import subprocess

channel_url = "https://www.youtube.com/c/GuilhermeMartinsTV/videos"
playlist_file = "playlist.m3u8"

with open(playlist_file, "w") as f:
    f.write("#EXTM3U\n")
    f.write("#EXT-X-VERSION:3\n")
    f.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")

    videos = subprocess.run(["yt-dlp", "--get-url", channel_url], stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")
    titles = subprocess.run(["yt-dlp", "--get-title", channel_url], stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")
    thumbnails = subprocess.run(["yt-dlp", "--get-thumbnail", channel_url], stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")

    for i in range(len(videos)):
        f.write(f"#EXTINF:-1 tvg-id=\"{titles[i]}\" tvg-logo=\"{thumbnails[i]}\",{titles[i]}\n")
        f.write(f"{videos[i]}\n")
