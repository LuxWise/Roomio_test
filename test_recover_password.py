import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


if len(sys.argv) != 2:
    print("❌ Uso: python test_recover_password_submit.py <correo>")
    sys.exit(1)

correo = sys.argv[1]

options = Options()
options.add_argument("--headless=new")  
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-infobars")
options.add_argument("--remote-debugging-port=9222")
options.add_argument("--window-size=1920,1080")
options.add_argument("--user-data-dir=/tmp/chrome-user-data") 

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.maximize_window()

try:
    # 1. Abrir la página de login
    driver.get("https://lux-wise.com/es/login")

    # 2. Hacer clic en "Recuperar"
    boton_recuperar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//h6[text()='Recuperar' and contains(@class, 'cursor-pointer')]"))
    )
    boton_recuperar.click()

    # 3. Esperar e ingresar correo en el input de recuperación
    input_correo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Correo de recuperación']"))
    )
    input_correo.send_keys(correo)

    # 4. Hacer clic en el botón "Enviar código"
    boton_enviar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//h6[contains(text(),'Enviar código')]]"))
    )
    boton_enviar.click()

    # 5. Esperar tras el envío
    time.sleep(5)

    print(f"✅ test recover password whit email '{correo}'.")

except Exception as e:
    print(f"❌ test recover password: {e}")

finally:
    driver.quit()
