import streamlink

# Abrir o arquivo BBVIPALBANIA.txt para leitura
with open("BBVIPALBANIA.txt", "r") as file:
    links = file.readlines()

# Remover o caractere de quebra de linha de cada link
links = [link.strip() for link in links]

# Para cada link no arquivo
for link in links:
    with streamlink.Streamlink() as session:
    session.set_option("twitch-disable-ads", True)
    session.set_option("twitch-disable-reruns", True)
    
    # Continue with your code here, using the `session` object instead of the `streamlink` module
    video_url = session.streams(link)["best"].url if session.streams(link) else None




    if video_url:
        # Gerar um novo arquivo com o streamlink
        filename = f"{link}.m3u8"
        with open(filename, "w") as file:
            file.write("#EXTM3U\n")
            file.write("#EXT-X-VERSION:3\n")
            file.write("#EXT-X-STREAM-INF:PROGRAM-ID=1,BANDWIDTH=5400000\n")
            file.write(video_url)
