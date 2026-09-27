# Pre Entrega Automation Testing - Saucedemo

## Descripción

Proyecto de automatización web desarrollado con Selenium WebDriver y Pytest.

El objetivo es validar funcionalidades básicas del sitio Saucedemo mediante pruebas automatizadas:

- Login de usuario
- Navegación del catálogo de productos
- Verificación de elementos de la interfaz
- Interacción con productos
- Agregado de productos al carrito de compras

## Tecnologías utilizadas

- Python
- Selenium WebDriver
- Pytest
- Pytest HTML
- WebDriver Manager
- Git
- GitHub


```

## Instalación

Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/pre-entrega-automation-testing-lopez-barbona.git
```

Ingresar al directorio:

```bash
cd pre-entrega-automation-testing-lopez-barbona
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Dependencias

El proyecto utiliza:

```text
selenium
pytest
pytest-html
webdriver-manager
```

## Casos de prueba implementados

### Login exitoso

- Acceso a Saucedemo
- Ingreso de credenciales válidas
- Verificación de redirección a inventory.html
- Validación del título "Products"

### Navegación y catálogo

- Validación del catálogo de productos
- Verificación de menú hamburguesa
- Verificación de filtro de productos
- Obtención del nombre y precio del primer producto

### Carrito de compras

- Agregado del primer producto al carrito
- Verificación del contador del carrito
- Acceso al carrito
- Validación del producto agregado

## Ejecución de pruebas

Ejecutar todas las pruebas:

```bash
pytest tests/test_saucedemo.py -v
```

## Generación de reporte HTML

Generar reporte HTML:

```bash
pytest tests/test_saucedemo.py -v --html=reports/reporte.html
```

El reporte generado se almacena en:

```text
reports/reporte.html
```

## Autor

Ivanna López Barbona