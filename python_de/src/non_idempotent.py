from data.orders_data import orders_data
try:
	# Works when executed as a package module.
	from .utils.data_transformations.transform_orders import transform_orders
except ImportError:
	# Fallback for direct script execution: python3 non_idempotent.py
	from utils.data_transformations.transform_orders import transform_orders

cleaned_orders = transform_orders(raw_orders=orders_data)
print(cleaned_orders)

cleaned_orders = transform_orders(raw_orders=orders_data)
print(cleaned_orders)