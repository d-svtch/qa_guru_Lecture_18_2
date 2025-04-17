import requests

API_URL = "https://demowebshop.tricentis.com/"


def product_add(API_cookie, product_id, quantity):
    response = requests.post(
        url=API_URL + f"addproducttocart/details/{product_id}/1",
        headers={'Cookie': f'Nop.customer={API_cookie}'},
        data={f'addtocart_{product_id}.EnteredQuantity': {quantity}},
    )
    return response

