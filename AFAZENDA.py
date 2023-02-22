import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# instantiate the Chrome driver
driver = webdriver.Chrome()

# navigate to the target URL
url_globoplay = "https://globoplay.globo.com/agora-na-tv/"
driver.get(url_globoplay)



# Configuring Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-gpu")



# Take 5 screenshots every 5 seconds
for i in range(5):
    driver.save_screenshot(f"screenshot{i+1}.png")
    time.sleep(9)
    
botao_assistir_agora = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Assista agora')]")))
botao_assistir_agora.click()
time.sleep(5)

campo_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "login")))
campo_senha = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.NAME, "password")))

campo_email.send_keys("bundadalele@gmail.com")
campo_senha.send_keys("minhasenhaéfoda97")

botao_entrar = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[contains(text(),'Entrar')]")))
botao_entrar.click()

# Aguardar alguns segundos para carregar todo o conteúdo da página
time.sleep(10)

# Get the page source to find the .m3u8 link
log_entries = driver.execute_script("return window.performance.getEntries();")

for entry in log_entries:
    if ".m3u8" in entry['name']:
        link = entry['name']
        break

# Close the driver
driver.quit()
