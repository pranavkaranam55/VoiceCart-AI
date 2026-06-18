import re


def extract_order(text):

    orders = []

    # Pattern 1:
    # 5 rice bags
    pattern1 = r'(\d+)\s+([a-zA-Z]+)'

    matches1 = re.findall(pattern1, text)

    for quantity, product in matches1:

        if product.lower() not in [
            "bags",
            "bag",
            "packets",
            "packet",
            "bottles",
            "bottle"
        ]:

            orders.append({
                "product": product.lower(),
                "quantity": int(quantity)
            })

    # Pattern 2:
    # 5 bags of rice
    pattern2 = r'(\d+)\s+\w+\s+of\s+([a-zA-Z]+)'

    matches2 = re.findall(pattern2, text)

    for quantity, product in matches2:

        orders.append({
            "product": product.lower(),
            "quantity": int(quantity)
        })

    return orders