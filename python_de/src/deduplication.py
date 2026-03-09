from .lists_filters import orders

order_ids = []
for order in orders:
    order_ids.append(order["orderNum"])

unique_order_ids = set(order_ids)
print(unique_order_ids)