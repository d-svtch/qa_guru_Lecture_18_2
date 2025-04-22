import requests
from allure_commons._allure import step
from jsonschema import validate
from schemas.schemas import product_added
from api_tools.api_tools import product_add, user_cookies
from ui_methods.ui_methods import check_cart

LOGIN = "example1200@example.com"
PASSWORD = "123456"
WEB_URL = "https://demowebshop.tricentis.com/"
API_URL = "https://demowebshop.tricentis.com/"


def test_add_product_to_cart():
    """API adding one product to cart"""
    product_1 = {"product_id": 31, "product_name": "14.1-inch Laptop", "quantity": 1}
    with step("Get API cookie"):
        auth_cookie = user_cookies(API_URL)
    with step("Ad product to cart"):
        result = product_add(auth_cookie, product_1["product_id"], product_1["quantity"])
        assert result.status_code == 200
        validate(result.json(), schema=product_added)
    with step("Check cart"):
        assert product_1["product_name"], product_1["quantity"] == check_cart(auth_cookie, product_1["product_name"], product_1["quantity"])

def test_add_amount_of_product():
    """API adding a few items of one product to cart"""
    product_1 = {"product_id": 31, "product_name": "14.1-inch Laptop", "quantity": 5}
    with step("Get API cookie"):
        auth_cookie = user_cookies(API_URL)
    with step("Ad product to cart"):
        result = product_add(auth_cookie, product_1["product_id"], product_1["quantity"])
        assert result.status_code == 200
        validate(result.json(), schema=product_added)
    with step("Check cart"):
        assert product_1["product_name"], product_1["quantity"] == check_cart(auth_cookie, product_1["product_name"], product_1["quantity"])

def test_add_various_products():
    """API adding a different products to cart"""
    products = [
        {"product_id": 31, "product_name": "14.1-inch Laptop", "quantity": 5},
        {"product_id": 43, "product_name": "Smartphone", "quantity": 3}
    ]
    with step("Get API cookie"):
        auth_cookie = user_cookies(API_URL)
    with step("Ad products to cart"):
        for product in products:
            result = product_add(auth_cookie, product["product_id"], product["quantity"])
            assert result.status_code == 200
            validate(result.json(), schema=product_added)
    with step("Check cart"):
        for product in products:
            assert product["product_name"], product["quantity"] == check_cart(auth_cookie, product["product_name"], product["quantity"])