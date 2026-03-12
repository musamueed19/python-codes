transformed_orders = []
def transform_orders(raw_orders):
    
    for order in raw_orders:
        transformed_orders.append({
            "order_id": order["id"].upper(),
            "customer_name": order["customer"]["name"].upper(),
            "total_amount": float(order["total"]),
            "items": [{
                "item_id": item["id"].upper(),
                "item_name": item["name"]
            } for item in order["items"]]
        })
        
    return transformed_orders
