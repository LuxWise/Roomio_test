import sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options


# Argumentos: correo y código de verificación
if len(sys.argv) != 3:
    print("❌ Uso: python test_full_registration.py <correo> <codigo_verificacion>")
    sys.exit(1)

correo = sys.argv[1]
codigo = sys.argv[2]

if not codigo.isdigit() or len(codigo) != 6:
    print("❌ El código debe tener exactamente 6 dígitos numéricos.")
    sys.exit(1)

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
    # 1. Página principal
    driver.get("https://lux-wise.com/es")

    # 2. Clic en "Registrarse"
    boton_registrarse = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[.//h6[contains(text(), 'Registrarse')]]"
        ))
    )
    boton_registrarse.click()

    # 3. Ingresar correo
    input_correo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Correo electrónico']"))
    )
    input_correo.send_keys(correo)
    time.sleep(2)

    # 4. Clic en "Proceder con el registro"
    boton_proceder = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH, "//button[.//h6[contains(text(),'Proceder con el registro')]]"
        ))
    )
    boton_proceder.click()

    # 5. Ingresar código de verificación
    input_codigo = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@inputmode='numeric']"))
    )
    input_codigo.send_keys(codigo)

    # 6. Completar el formulario
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//input[@placeholder='Nombre']"))
    ).send_keys("Luis")

    driver.find_element(By.XPATH, "//input[@placeholder='Apellido']").send_keys("Solano")
    driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("3001234567")
    driver.find_element(By.XPATH, "//input[@placeholder='Contraseña']").send_keys("Test1234*")
    driver.find_element(By.XPATH, "//input[@placeholder='Confirmar contraseña']").send_keys("Test1234*")

    time.sleep(5)

    # 7. Clic en "Registro de Usuario"
    boton_final = driver.find_element(By.XPATH, "//button[.//h6[contains(text(),'Registro de Usuario')]]")
    boton_final.click()

    # 8. Esperar redirección final
    time.sleep(10)

    print("✅test register")

except Exception as e:
    print(f"❌ test register: {e}")

finally:
    driver.quit()
