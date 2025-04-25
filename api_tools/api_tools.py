import json
import requests
from allure_commons.types import AttachmentType
import allure

API_URL = "https://demowebshop.tricentis.com/"


def product_add(api_cookie, product_id, quantity):
    response = requests.post(
        url=API_URL + f"addproducttocart/details/{product_id}/1",
        headers={'Cookie': f'Nop.customer={api_cookie}'},
        data={f'addtocart_{product_id}.EnteredQuantity': {quantity}},
    )
    allure.attach(body=json.dumps(response.json(), indent=4, ensure_ascii=True), name="Product added to cart",
                  attachment_type=AttachmentType.JSON, extension="json")

    return response

def user_cookies(url):
    response = requests.get(url).cookies.get("Nop.customer")
    allure.attach(body=str(response), name="Cookies",
                  attachment_type=allure.attachment_type.TEXT, extension="txt")
    return response