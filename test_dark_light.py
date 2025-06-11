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
    # 1. Cargar la página
    driver.get("https://lux-wise.com/es")

    # 2. Esperar que el SVG del sol sea visible
    svg_sol = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[contains(@id, 'sun')]"))
    )

    # 3. Hacer clic vía JavaScript para evitar errores comunes con SVGs
    driver.execute_script("arguments[0].click();", svg_sol)

    # 4. Esperar visualmente para observar el cambio
    time.sleep(5)

    print("✅ test dark ligth")

except Exception as e:
    print(f"❌ test dark ligth: {e}")

finally:
    driver.quit()
