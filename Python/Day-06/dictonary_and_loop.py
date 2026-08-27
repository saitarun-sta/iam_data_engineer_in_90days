orders = [
    {"id": 1, "customer": "Asha", "amount": 2500},
    {"id": 2, "customer": "Rahul", "amount": 800},
    {"id": 3, "customer": "Priya", "amount": 3200},
]

for order in orders:
    if order["amount"] > 2000:
        print(f"{order["customer"]} {order["amount"]}")
