from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

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
    # 1. Ir a la página de confirmación en español
    driver.get("https://lux-wise.com/es/login/recover/success")

    # 2. Hacer clic en el ícono del mundo para mostrar el menú de idiomas
    trigger = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'cursor-pointer')]"))
    )
    trigger.click()

    # 3. Esperar a que aparezca el menú flotante y seleccionar "en"
    language_menu = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'absolute') and contains(@class, 'flex-col') and contains(@class, 'bg-[#232946]')]"))
    )

    button_en = language_menu.find_element(By.XPATH, ".//button[contains(text(),'en')]")
    button_en.click()

    # 4. Esperar a que cargue la nueva página y verificar el texto en inglés
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.TAG_NAME, "h2"), "Congratulations!")
    )

    print("✅ test notification language")

except Exception as e:
    print(f"❌ test notification language: {e}")

finally:
    driver.quit()
