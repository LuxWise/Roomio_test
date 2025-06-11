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

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # 1. Abrir la página
    driver.get("https://lux-wise.com/es")

    # 2. Esperar a que el botón sea visible (no solo presente)
    boton_mapa = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((
            By.XPATH,
            "//div[contains(@class, 'bg-white') and contains(@class, 'cursor-pointer') and contains(@class, 'h-12') ]"
        ))
    )

    # 3. Hacer scroll hasta el botón por si está fuera de vista
    driver.execute_script("arguments[0].scrollIntoView(true);", boton_mapa)
    time.sleep(1)  # Pausa corta para que sea visible

    # 4. Hacer clic
    boton_mapa.click()

    # 5. Esperar visualmente después del clic
    time.sleep(10)

    print("✅ test map")

except Exception as e:
    print(f"❌ test map: {e}")

finally:
    driver.quit()
