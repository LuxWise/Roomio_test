from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

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
    # 1. Ir a la página principal en español
    driver.get("https://lux-wise.com/es")

    # 2. Hacer clic en el selector de destino
    destino_trigger = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((
            By.XPATH,
            "//div[contains(@class, 'cursor-pointer') and contains(., 'Destino') and contains(., 'Seleccionar destino')]"
        ))
    )
    destino_trigger.click()

    # 3. Esperar que aparezca la lista y hacer clic en "Colombia"
    primer_destino = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//ul/li[contains(text(),'Colombia')]"))
    )
    primer_destino.click()

    # 4. Esperar y hacer clic en el botón de búsqueda (flecha azul)
    boton_buscar = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'bg-[#587aff]') and contains(@class, 'cursor-pointer')]"))
    )
    boton_buscar.click()

    # 5. Esperar 5 segundos después del clic
    time.sleep(5)

    print("✅ test destination")

except Exception as e:
    print(f"❌ test destination: {e}")

finally:
    driver.quit()
