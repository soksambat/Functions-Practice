# EX8.Create function to sum total of price 
# products = [
#     {"name": "Apple", "price": 20},
#     {"name": "Orange", "price": 24},
# ]

def sum_total_price(products):
    return sum(product['price'] for product in products)
products = [
    {"name": "Apple", "price": 20},
    {"name": "Orange", "price": 24},
]
print(sum_total_price(products))  