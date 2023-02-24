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

# URL da página desejada para extração da .m3u8
url_playplus = "https://www.playplus.com/live/liveEvent/249"

# Abrir a página desejada após o login
driver.get(url_playplus)

# Esperando o vídeo ser carregado e reproduzido
time.sleep(5)

# Obter o conteúdo da página
html_content = driver.page_source

# Encontrar o link .m3u8 na página
start_index = html_content.find("var urlLive = '") + 15
end_index = html_content.find("';", start_index)
link = html_content[start_index:end_index]
print(link)

# Fechar o driver
driver.quit()

import os
os.environ["EMAILPLAYPLUS"] = "seu-email-aqui"
print(os.getenv("EMAILPLAYPLUS"))
