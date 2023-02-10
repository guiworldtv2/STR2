import requests
from bs4 import BeautifulSoup
import time

# URL da página
url = 'https://www.twitch.tv/search?term=bbvip'

# Fazendo a requisição e obtendo o HTML da página
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

# Esperando 10 segundos antes de fazer a coleta dos links
time.sleep(10)

# Encontrando todas as tags <a> com a classe "ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link"
links = soup.find_all('a', {'class': 'ScCoreLink-sc-16kq0mq-0 fQAQWb tw-link'})

# Concatenando a URL base "https://www.twitch.tv" com o atributo href de cada tag <a>
urls = ['https://www.twitch.tv' + link.get('href') for link in links]

# Escrevendo os links no arquivo BBVIPALBANIA.txt
with open("BBVIPALBANIA.txt", "w") as f:
    for url in urls:
        f.write(url + '\n')
