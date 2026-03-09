# List of Dictionaries (2 Key-Value Pair)/Dict
orders = [
    {
        "orderNum": 1,  "country": "PAK"
    },
    {
        "orderNum": 2,  "country": "US"
    },
    {
        "orderNum": 3,  "country": "US"
    },
]



# filter "PAK" Country orders (only)
pak_orders = []

for order in orders:
    if order["country"] == "PAK":
        pak_orders.append(order)
        
print(pak_orders)