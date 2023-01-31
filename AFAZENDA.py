import subprocess
import os

# Lê o arquivo AFAZENDA.txt
with open("AFAZENDA.txt", "r") as f:
    links = f.readlines()

# Remove o caractere de nova linha (\n) ao final de cada linha
links = [link.strip() for link in links]

# Contador para os nomes dos arquivos
counter = 1

# Loop para cada link do arquivo
for link in links:
    try:
        # Obter informações dos vídeos usando o yt-dlp
        title = subprocess.run(["yt-dlp", "--get-title", link], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
        thumbnail = subprocess.run(["yt-dlp", "--get-thumbnail", link], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
        video_url = subprocess.run(["yt-dlp", "--get-url", link], stdout=subprocess.PIPE).stdout.decode("utf-8").strip()
    except:
        try:
            # Obter informações dos vídeos usando o youtube-dl
            info = subprocess.run(["youtube-dl", "--get-title", "--get-thumbnail", "--get-url", link], stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")
            title = info[0]
            thumbnail = info[1]
            video_url = info[2]
        except:
            try:
                # Obter informações dos vídeos usando o streamlink
                info = subprocess.run(["streamlink", "--get-title", "--get-thumbnail", "--get-url", link], stdout=subprocess.PIPE).stdout.decode("utf-8").strip().split("\n")
                title = info[0]
                thumbnail = info[1]
                video_url = info[2]
            except:
                print(f"Não foi possível obter informações do link {link}")
                continue

    # Salva as informações obtidas em um arquivo
    with open(f"MEULINK{counter}.txt", "w") as f:
        f.write(f"#EXTM3U\n")
        f.write(f"#EXT-X-VERSION:3\n")
        f.write(f"#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=2560000\n")
        f.write(f'#EXTINF:-1 tvg-id="{title}" tvg-logo="{thumbnail}",{title}\n')
        f.write(f"{video_url}\n")

    #
