import requests
from bs4 import BeautifulSoup

# Realiza a requisição da página
url = "https://www.twitch.tv/search?term=bbvip"
response = requests.get(url)

# Extrai o conteúdo HTML da página
soup = BeautifulSoup(response.content, "html.parser")

# Encontra todos os elementos <a> com a classe especificada
links = soup.find_all("a", class_="ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link")

# Adiciona "https://www.twitch.tv" antes de cada href
formatted_links = ["https://www.twitch.tv" + link["href"] for link in links]

# Escreve os links formatados em um arquivo chamado "BBVIPALBANIA.txt"
try:
    with open("BBVIPALBANIA.txt", "w") as file:
        for link in formatted_links:
            file.write(link + "\n")
    print("Links capturados e escritos no arquivo BBVIPALBANIA.txt.")
except:
    print("Ocorreu um erro ao escrever no arquivo.")
