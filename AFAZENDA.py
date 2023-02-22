from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Define o serviço para o driver
service = ChromeService(executable_path='caminho/para/o/driver/chromedriver.exe')

# Inicializa o driver
driver = webdriver.Chrome(service=service)

# Abre a página
driver.get("https://globoplay.globo.com/agora-na-tv/")

# Take 5 screenshots every 5 seconds
for i in range(5):
    driver.save_screenshot(f"screenshot{i+1}.png")
    time.sleep(9)
    
    
botao_assistir_agora = driver.find_element_by_xpath("//button[contains(text(),'Assista agora')]")
botao_assistir_agora.click()
time.sleep(5)

campo_email = driver.find_element_by_name("login")
campo_senha = driver.find_element_by_name("password")

campo_email.send_keys("bundadalele@gmail.com")
campo_senha.send_keys("minhasenhaéfoda97")

botao_entrar = driver.find_element_by_xpath("//button[contains(text(),'Entrar')]")
botao_entrar.click()
# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(5)

# Get the page source to find the .m3u8 link
log_entries = driver.execute_script("return window.performance.getEntries();")

for entry in log_entries:
    if ".m3u8" in entry['name']:
        link = entry['name']
        break

# Close the driver
driver.quit()



    





