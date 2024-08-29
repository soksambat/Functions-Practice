# EX9.Create function to find average of price
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def average_price(products):
    total_price = sum(product['price'] for product in products)
    count = len(products)
    return total_price / count if count > 0 else 0
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(average_price(products))  