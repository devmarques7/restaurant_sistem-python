from menu import products


def get_product_by_id(id: int):
    if type(id) == int:
        for item in products:
            if item['_id'] == id:
                return item
        return {}
    raise TypeError("product id must be an int")


def get_products_by_type(type_product: str):

    if type(type_product) == str:
        list_of_types = []
        for item in products:
            if type_product == item["type"]:
                list_of_types.append(item)
        if len(list_of_types):
            return list_of_types
        return list()
    raise TypeError("product type must be a str")


def menu_report():
    product_count = len(products)
    avarage_price = 0
    most_commun_type = products[0]["type"]
    for items in products:
        avarage_price += items['price']
        if len(get_products_by_type(most_commun_type)) < len(get_products_by_type(items["type"])):
            most_commun_type = items["type"]
    avarage_price = avarage_price / product_count

    return f"Products Count: {product_count} - Average Price: ${avarage_price:.1f} - Most Common Type: {most_commun_type}"


def add_product(cart, **product):
    id = len(cart) + 1
    product["_id"] = id
    cart.append(product)
    return product
