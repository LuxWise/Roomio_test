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
    # 1. Abrir la página
    driver.get("https://lux-wise.com")

    # 2. Clic en el ícono que despliega el selector de idiomas
    trigger = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'cursor-pointer')]"))
    )
    trigger.click()

    # 3. Esperar que aparezca el menú flotante
    language_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'absolute') and contains(@class, 'flex-col') and contains(@class, 'bg-[#232946]')]"))
    )

    time.sleep(5)


    # 4. Hacer clic en el botón "es"
    button_es = language_menu.find_element(By.XPATH, ".//button[contains(text(),'es')]")
    button_es.click()

    time.sleep(5)


    print("✅ test language switch")

except Exception as e:
    print(f"❌ test language switch: {e}")

finally:
    driver.quit()
