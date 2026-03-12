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

if __name__ == "__main__":
    try:
        from data.orders_data import orders_data
    except ModuleNotFoundError:
        import os
        import sys

        # Allow direct script execution from nested path by adding src to sys.path.
        src_root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
        if src_root not in sys.path:
            sys.path.insert(0, src_root)
        from data.orders_data import orders_data

    cleaned_orders = transform_orders(raw_orders=orders_data)
    print(cleaned_orders)