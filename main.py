from management import get_product_by_id, get_products_by_type, menu_report, add_product, calculate_tab


cart = []
product = {
    "description": "Healthy breakfast with cottage cheese and strawberry",
    "price": 14.05,
    "rating": 1,
    "title": "Breakfast with cottage",
    "type": "fruit",
}

if __name__ == "__main__":
    # try:
    #     print(get_product_by_id(23))

    # except TypeError as error:
    #     print(f'Error: {error}')

    # print(get_product_by_type("drink"))
    # print(menu_repost())

    # print(get_product_by_id(1))

    print(add_product(cart, **product))
