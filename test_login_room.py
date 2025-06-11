import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

if len(sys.argv) != 3:
    print("Uso: python test_room_login_flow.py <correo> <contraseña>")
    sys.exit(1)

correo_usuario = sys.argv[1]
contrasena_usuario = sys.argv[2]

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
    # 1. Ir a la página principal
    driver.get("https://lux-wise.com/es")

    # 2. Clic en la tarjeta del hotel
    tarjeta_hotel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//div[contains(@class, 'relative') and contains(@class, 'cursor-pointer') and .//img[contains(@src, 'hotelexample (1).jpg')]]"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tarjeta_hotel)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", tarjeta_hotel)

    # 3. Esperar redirección
    time.sleep(2)

    # 4. Clic en el botón de login para reservar
    boton_reserva = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//button[contains(@class, 'bg-green-600') and .//h6[contains(text(), 'Inicia sesión para reservar')]]"
        ))
    )
    boton_reserva.click()
    time.sleep(3)

    # 5. Llenar el formulario de inicio de sesión
    input_email = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Correo electrónico']"))
    )
    input_email.send_keys(correo_usuario)

    input_password = driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']")
    input_password.send_keys(contrasena_usuario)

    # 6. Clic en "Ingresar en Roomio"
    boton_ingresar = driver.find_element(By.XPATH, "//button[.//h6[contains(text(), 'Ingresar en Roomio')]]")
    boton_ingresar.click()

    time.sleep(2)

    tarjeta_hotel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//div[contains(@class, 'relative') and contains(@class, 'cursor-pointer') and .//img[contains(@src, 'hotelexample (2).jpg')]]"
        ))
    )
    driver.execute_script("arguments[0].scrollIntoView(true);", tarjeta_hotel)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", tarjeta_hotel)

    time.sleep(5)

    print("✅ test room login flow: completado")

except Exception as e:
    print(f"❌ test room login flow: {e}")

finally:
    driver.quit()
