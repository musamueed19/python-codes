from data.orders_data import orders_data
from utils.data_transformations.transform_orders import transform_orders

transformed_orders = transform_orders(raw_orders=orders_data)
print(transformed_orders)