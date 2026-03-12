import ast
import pandas as pd

df = pd.read_csv("data/raw/raw_orders.csv")

df["total_amount"] = df["total_amount"].fillna(0)
df["total_amount"] = df["total_amount"].astype(float)
df["order_id"] = df["order_id"].astype(int)
df["customer_name"] = df["customer_name"].str.upper()
df["items"] = df["items"].apply(ast.literal_eval)
df["country"] = df["country"].astype(str)

print(df)

country_summary = (
    df.groupby("country")["total_amount"]
    .agg(["sum", "mean", "count"])
    .rename(columns={"sum": "total_sales", "mean": "average_order_value", "count": "order_count"})
    .reset_index()
)

country_simple_summary = (
    df.groupby("country")
    .agg(
        total_orders=("order_id", "count"),
        total_sales=("total_amount", "sum"),
        max_order_value=("total_amount", "max")
    )   
)

print(country_simple_summary)