import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from utils.helpers import (
    login,
    esperar_inventario,
    obtener_primer_producto
)


@pytest.fixture
def driver():
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )

    driver.maximize_window()

    yield driver

    driver.quit()


# TEST 1 - LOGIN
def test_login_exitoso(driver):

    login(driver)

    esperar_inventario(driver)

    assert "inventory.html" in driver.current_url

    titulo = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text

    assert titulo == "Products"


# TEST 2 - CATALOGO
def test_catalogo_productos(driver):

    login(driver)

    esperar_inventario(driver)

    titulo = driver.find_element(
        By.CLASS_NAME,
        "title"
    ).text

    assert titulo == "Products"

    productos = driver.find_elements(
        By.CLASS_NAME,
        "inventory_item"
    )

    assert len(productos) > 0

    menu = driver.find_element(
        By.ID,
        "react-burger-menu-btn"
    )

    filtro = driver.find_element(
        By.CLASS_NAME,
        "product_sort_container"
    )

    assert menu.is_displayed()
    assert filtro.is_displayed()

    nombre, precio = obtener_primer_producto(driver)

    print(f"\nPrimer producto: {nombre}")
    print(f"Precio: {precio}")

    assert nombre != ""
    assert precio != ""


# TEST 3 - CARRITO
def test_agregar_producto_carrito(driver):

    login(driver)

    esperar_inventario(driver)

    nombre_producto = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    driver.find_element(
        By.XPATH,
        "(//button[contains(text(),'Add to cart')])[1]"
    ).click()

    contador = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "shopping_cart_badge")
        )
    )

    assert contador.text == "1"

    driver.find_element(
        By.CLASS_NAME,
        "shopping_cart_link"
    ).click()

    producto_carrito = driver.find_element(
        By.CLASS_NAME,
        "inventory_item_name"
    ).text

    assert producto_carrito == nombre_producto
    
    