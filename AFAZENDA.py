from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import secrets 

# URL da página de login
url_playplus_login = "https://www.playplus.com/Account/Login"

# Criando as opções para o chrome
options = Options()
options.add_argument("--window-size=1920,1080") # set screen size to 1920x1080
options.add_argument("--headless")
options.add_argument("--disable-gpu")

# Instanciando o driver do chrome
driver = webdriver.Chrome(options=options)

# Abrir a página de login do PlayPlus
driver.get(url_playplus_login)

# Take 5 screenshots every 5 seconds
for i in range(5):
    driver.save_screenshot(f"screenshot{i+1}.png")
    time.sleep(9)

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(15)

# Esperar até que os campos de e-mail e senha estejam presentes na página
email_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "UserName")))

# Preencher o campo de e-mail com a informação desejada
email_field.send_keys("oquefoiagora@hotmail.com")

# Preencher o campo de senha com a informação desejada
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Password")))
password_field.send_keys("ratosdeporao062")

# Localizar e clicar no botão "Avançar"
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='redirect btn btn-primary btn-block btn-login btn-next']")))
login_button.click()

# Localizar e clicar no botão do perfil do usuário
profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='profile redirect']")))
profile_button.click()

# Esperando a página ser carregada após clicar no perfil do usuário
time.sleep(10)


time.sleep(10)
#URL da página desejada para extração da .m3u8

url_playplus = "https://www.playplus.com/live"
Abrir a página desejada após o login

driver.get(url_playplus)
#Esperando a página ser carregada

time.sleep(10)
#Encontrar todos os links para os eventos ao vivo

live_links = driver.find_elements_by_xpath("//a[@class='no-decoration']")
#Criar um dicionário para armazenar os links e subtemas dos canais

channel_links = {}
#Para cada link, obter as informações necessárias

for link in live_links:
# Obter o ID do evento ao vivo
event_id = link.get_attribute("href").split("/")[-1]

# Obter o subtema do canal
subtheme = link.find_element_by_xpath(".//div[@class='pl-2 pr-2 mb-0 span-view title now']")
subtheme = subtheme.text.strip()

# Obter o nome do canal
channel_name = link.find_element_by_xpath(".//img[@class='live-slider img-fluid thumbnail m-auto d-block now']")
channel_name = channel_name.get_attribute("data-sname")

# Iterando sobre as URLs dos eventos ao vivo
for url in url_list:
    # Abrir a página do evento ao vivo
    driver.get(url)

    # Obter o conteúdo da página
    html_content = driver.page_source

    # Encontrar o link .m3u8 na página
    start_index = html_content.find("var urlLive = '") + 15
    end_index = html_content.find("';", start_index)
    link = html_content[start_index:end_index]
    channel_name = html_content.find("data-sname=\"") + 12
    channel_name_end = html_content.find("\"", channel_name)
    channel_name = html_content[channel_name:channel_name_end]

    # Adicionar o link na lista de links de canais
    channel_links.append((channel_name, "https://www.playplus.com" + link))

# Fechar o driver
driver.quit()
# Criar o arquivo .m3u8 com os links dos canais
with open("playplus_channels.m3u8", "w") as f:
    # Escrever o cabeçalho do arquivo
    f.write("#EXTM3U\n")
    for channel_link in channel_links:
        # Escrever o link do canal no formato EXTINF
        f.write(f"#EXTINF:-1,tvg-logo=\"{channel_link[0]}\",{channel_link[0]} - {channel_link[1]}\n{channel_link[1]}\n")
