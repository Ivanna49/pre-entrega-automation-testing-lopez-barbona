from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

URL = "https://www.saucedemo.com/"


def login(driver):

    driver.get(URL)

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()


def esperar_inventario(driver):

    WebDriverWait(driver, 10).until(
        EC.url_contains("inventory.html")
    )


def obtener_primer_producto(driver):

    nombre = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    precio = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_price"
    ).text

    return nombre, precio