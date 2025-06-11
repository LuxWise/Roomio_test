import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import SessionNotCreatedException, WebDriverException
from selenium.webdriver.chrome.options import Options

if len(sys.argv) != 3:
    print("Uso: python test_room_login_mobile.py <correo> <contraseña>")
    sys.exit(1)

correo = sys.argv[1]
clave = sys.argv[2]

# 📱 Emulación móvil
mobile_emulation = {
    "deviceName": "iPhone 12 Pro"
}

options = Options()
options.add_experimental_option("mobileEmulation", mobile_emulation)

# 🐳 Opciones para compatibilidad con Docker
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-extensions")
options.add_argument("--disable-application-cache")
options.add_argument("--disable-infobars")
options.add_argument("--remote-debugging-port=9222")

# 🧪 Corrección: sin --window-size (lo fuerza el emulador móvil)

try:
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    driver.get("https://lux-wise.com/es")

    # Clic en la tarjeta del hotel
    hotel_card = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@class, 'relative') and .//img[contains(@src, 'hotelexample (2).jpg')]]"))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", hotel_card)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", hotel_card)
    time.sleep(5)

    # Clic en botón "Inicia sesión para reservar"
    boton_login = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[.//h6[contains(text(), 'Inicia sesión para reservar')]]"))
    )
    boton_login.click()
    time.sleep(2)

    # Llenar login
    input_email = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Correo electrónico']")))
    input_email.send_keys(correo)

    input_password = driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']")
    input_password.send_keys(clave)

    btn_ingresar = driver.find_element(By.XPATH, "//button[.//h6[contains(text(), 'Ingresar en Roomio')]]")
    btn_ingresar.click()

    time.sleep(5)

    # 🎯 Captura final (si todo va bien)
    driver.save_screenshot("success_mobile_test.png")
    print("📸 Captura guardada en success_mobile_test.png")
    print("✅ test_room_login_mobile: Éxito")

except SessionNotCreatedException as e:
    print("❌ Error de sesión: Versión incompatible de Chrome o conflicto de sesión.")
    print(f"Detalles: {e}")
    driver.save_screenshot("error_mobile_test.png")

except WebDriverException as e:
    print("❌ Error de WebDriver:")
    print(f"Detalles: {e}")
    driver.save_screenshot("error_mobile_test.png")

except Exception as e:
    print(f"❌ Otro error inesperado: {e}")
    driver.save_screenshot("error_mobile_test.png")

finally:
    driver.quit()
