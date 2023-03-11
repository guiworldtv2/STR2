from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import secrets 
import re

# Criando as opções para o chrome
options = Options()
options.add_argument("--window-size=1920,1080") # set screen size to 1920x1080
options.add_argument("--headless")
options.add_argument("--disable-gpu")


# URL da página de login
url_playplus_login = "https://www.playplus.com/Account/Login"

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
email_field.send_keys("{A}")

# Preencher o campo de senha com a informação desejada
password_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "Password")))
password_field.send_keys("{B}")

# Localizar e clicar no botão "Avançar"
login_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@class='redirect btn btn-primary btn-block btn-login btn-next']")))
login_button.click()

# Localizar e clicar no botão do perfil do usuário
profile_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='profile redirect']")))
profile_button.click()

# Esperando a página ser carregada após clicar no perfil do usuário
time.sleep(10)

# URL da página desejada para extração da .m3u8
url_playplus = "https://www.playplus.com/live"

# Abrir a página desejada após o login
driver.get(url_playplus)

# Enquanto o botão "Próximo" estiver habilitado, continuar extraindo os links .m3u8
while True:
    # Encontra todos os elementos <a> com a classe 'no-decoration'
    links = driver.find_elements(By.CSS_SELECTOR, 'div.row.slick-slide.slick-current.slick-active a.no-decoration')

    # Itera sobre os links encontrados e acessa cada um para extrair o link .m3u8
    for link in links:
        href = link.get_attribute('href')
        name = link.find_element(By.CSS_SELECTOR, 'img.now').get_attribute('data-sname')
        thumbnail = link.find_element(By.CSS_SELECTOR, 'img.now').get_attribute('src')
        subtitle = link.find_element(By.CSS_SELECTOR, 'img.now').get_attribute('data-name')

        # Entra no link para extrair o link .m3u8
        driver.get(href)
        time.sleep(5)  # espera 5 segundos para garantir que a página carregue completamente
        html_content = driver.page_source
        start_index = html_content.find("var urlLive = '") + 15
        end_index = html_content.find("';", start_index)
        m3u8_link = html_content[start_index:end_index]

        # Imprime o link .m3u8
        print(f'#EXTINF:-1 group-title="PLAYPLUS" tvg-logo="{thumbnail}",{name} - {subtitle}\n{m3u8_link}\n')

        # Volta para a página anterior
        driver.execute_script("window.history.go(-1)")
        time.sleep(5)  # espera 5 segundos para garantir que a página carregue completamente
    
    # Verifica se o botão "Próximo" está presente na página
    next_button = driver.find_elements(By.CSS_SELECTOR, 'a.next')
    if next_button:
        # Clica no botão "Próximo" para acessar a próxima página
        next_button[0].click()
        time.sleep(5)  # espera 5 segundos para garantir que a página carregue completamente
    else:
        break  # Sai do loop se o botão "Próximo" não estiver presente

# Encerra o driver do Chrome
driver.quit()

