# Get the page source again after scrolling to the bottom
html_content = driver.page_source

# Find the links and titles of the videos found
try:
    soup = BeautifulSoup(html_content, "html.parser")
    videos = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 jKBAWW tw-link", href=True)
    links = ["https://www.twitch.tv" + video.get("href") for video in videos]
    channels = [video.find("p", {"data-a-target": "preview-card-channel-link", "class": "CoreText-sc-1txzju1-0 jiepBC"}).get("title") for video in videos]
    titles = [video.find("h3", class_="CoreText-sc-1txzju1-0 eJuFGD").get("title") for video in videos]
except Exception as e:
    print(f"Erro: {e}")
finally:
    # Close the driver
    driver.quit()




# Instalando streamlink
subprocess.run(['pip', 'install', '--user', '--upgrade', 'streamlink'])

# Get the playlist and write to file
try:
    with open('./TWITCHPLAY.m3u', 'w') as f:
        f.write("#EXTM3U\n")  # Imprime #EXTM3U uma vez no início do arquivo
        for i, link in enumerate(links):
            # Get the stream information using streamlink
            streams = streamlink.streams(link)
            url = streams['best'].url

            # Write the stream information to the file
            title = channels[i]
            f.write(f"#EXTINF:-1 tvg-id='{title}' group-title=\"TWITCH\",{title}\n")           
            f.write(f"{url}\n")
            f.write("\n")
except Exception as e:
    print(f"Erro ao criar o arquivo .m3u8: {e}")
