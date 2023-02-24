from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# URL da página de login
url_playplus_login = "https://www.playplus.com/Account/Login"

# Configuração do driver
options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')


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


# URL da página de transmissões ao vivo
url_live = "https://www.playplus.com/live"


# Esperar o login ser efetuado
time.sleep(5)

# Acessar a página de transmissões ao vivo
driver.get(url_live)

# Esperar a página ser carregada
time.sleep(5)

# Extrair informações de cada transmissão
transmissions = driver.find_elements_by_xpath("//a[contains(@class, 'no-decoration') and contains(@href, '/live/liveEvent/')]")

for transmission in transmissions:
    # Extrair informações da transmissão
    name = transmission.find_element_by_xpath(".//div[contains(@class, 'span-view') and contains(@class, 'title')]").text
    thumbnail = transmission.find_element_by_xpath(".//img").get_attribute("src")
    link = "https://www.playplus.com" + transmission.get_attribute("href")
    
    # Acessar a página da transmissão
    driver.get(link)

    # Esperar o vídeo ser carregado e reproduzido
    time.sleep(5)

    # Obter o conteúdo da página
    html_content = driver.page_source

    # Encontrar o link .m3u8 na página
    start_index = html_content.find("var urlLive = '") + 15
    end_index = html_content.find("';", start_index)
    m3u8_link = html_content[start_index:end_index]

    # Gerar arquivo .m3u8 para a transmissão
    file_name = name.replace(" ", "_").lower() + ".m3u8"
    with open(file_name, "w") as f:
        f.write("#EXTM3U\n#EXTINF:-1," + name + "\n" + m3u8_link)

    # Imprimir o link da thumbnail
    print("Transmissão:", name)
    print("Link da thumbnail:", thumbnail)
    print("Link .m3u8:", m3u8_link)
    print()

# Fechar o driver
driver.quit()
