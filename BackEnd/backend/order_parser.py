import re

IGNORE_WORDS = {
    "packet", "packets",
    "bottle", "bottles",
    "bag", "bags",
    "piece", "pieces",
    "box", "boxes",
    "of"
}


def extract_order(text):

    orders = []

    text = text.lower()

   
    pattern = r'(\d+)\s+([a-zA-Z]+(?:\s+[a-zA-Z]+){0,2})'

    matches = re.findall(pattern, text)

    for quantity, phrase in matches:

        words = phrase.split()

        filtered_words = [
            word for word in words
            if word not in IGNORE_WORDS
        ]

        if len(filtered_words) == 0:
            continue

        product = filtered_words[-1]

        orders.append({
            "product": product,
            "quantity": int(quantity)
        })

    merged_orders = {}

    for item in orders:

        product = item["product"]
        quantity = item["quantity"]

        if product in merged_orders:
            merged_orders[product] += quantity
        else:
            merged_orders[product] = quantity

    final_orders = []

    for product, quantity in merged_orders.items():

        final_orders.append({
            "product": product,
            "quantity": quantity
        })

    return final_orders