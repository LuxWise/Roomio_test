from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()

try:
    # 1. Abrir página principal
    driver.get("https://lux-wise.com/es")

    # 2. Esperar que esté presente el div contenedor (aunque no clickeable aún)
    tarjeta_hotel = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH,
            "//div[contains(@class, 'relative') and contains(@class, 'cursor-pointer') and .//img[contains(@src, 'hotelexample (2).jpg')]]"
        ))
    )

    # 3. Hacer scroll hasta él y clic con JavaScript
    driver.execute_script("arguments[0].scrollIntoView(true);", tarjeta_hotel)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", tarjeta_hotel)

    # 4. Esperar la redirección
    time.sleep(5)

    print("✅ test room details")

except Exception as e:
    print(f"❌ test room details: {e}")

finally:
    driver.quit()
