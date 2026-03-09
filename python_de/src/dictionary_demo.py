raw_api_response = {
    "order_id": 101,
    "customer": {
        "name": "Muhammad Musa Mueed",
        "cust_id": 219
    },
    "items": [
        {
            "sku": "P102",
            "price": 149,
            "quantity": 2
        },
        {
            "sku": "P456",
            "price": 89,
            "quantity": 12
        },
    ],
    "country": "PAK"
}



structured_order = {
    "order_id": raw_api_response["order_id"],
    "customer_id": raw_api_response["customer"]["cust_id"],
    "customer_name": raw_api_response["customer"]["name"],
    "order_items": raw_api_response["items"],
    "total_amount": sum(item["price"]*item["quantity"] for item in raw_api_response["items"]),
    "order_origin_country": raw_api_response["country"]
}

print(structured_order)