# EX10.Show product name that has maximum price
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def max_price_product(products):
    return max(products, key=lambda product: product['price'])['name']
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(max_price_product(products))  