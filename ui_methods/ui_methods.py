from allure_commons._allure import step
from selene import browser
from selene import query

API_URL = "https://demowebshop.tricentis.com/"


def check_cart(cookie, product_name, quantity):
    browser.open(API_URL + "cart")
    browser.driver.add_cookie({"name": "Nop.customer", "value": cookie})
    browser.open(API_URL + "cart")
    with step(f"Verify '{product_name}' with quantity {quantity} in cart"):
        items = browser.all('.cart-item-row')  # заменяй на актуальный селектор обёртки товара

        for item in items:
            name = item.element('.product-name').get(query.text).strip()
            qty = item.element('.qty-input').get(query.value)

            if name == product_name and int(qty) == quantity:
                return