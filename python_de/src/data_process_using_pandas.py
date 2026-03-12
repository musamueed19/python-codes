import pandas as pd

df = pd.DataFrame({
    "order_id": range(1, 11),
    "customer_name": ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy"],
    "total_amount": [100.0, 150.5, 200.0, 250.75, 300.0, 350.25, 400.0, 450.5, None, 550.75],
    "items": [
        [{"item_id": "A1", "item_name": "Widget"}, {"item_id": "A2", "item_name": "Gadget"}],
        [{"item_id": "B1", "item_name": "Thingamajig"}],
        [{"item_id": "C1", "item_name": "Doohickey"}, {"item_id": "C2", "item_name": "Whatsit"}, {"item_id": "C3", "item_name": "Contraption"}],
        [{"item_id": "D1", "item_name": "Gizmo"}],
        [{"item_id": "E1", "item_name": "Doodad"}, {"item_id": "E2", "item_name": "Thingy"}],
        [{"item_id": "F1", "item_name": "Widget Pro"}],
        [{"item_id": "G1", "item_name": "Gadget Plus"}, {"item_id": "G2", "item_name": "Gizmo Max"}],
        [{"item_id": "H1", "item_name": "Doohickey Deluxe"}],
        [{"item_id": "I1", "item_name": "Whatsit Ultra"}, {"item_id": "I2", "item_name": "Contraption Extreme"}],
        [{"item_id": "J1", "item_name": "Doodad Pro"}, {"item_id": "J2", "item_name": "Thingy Plus"}, {"item_id": "J3", "item_name": "Widget Max"}]
    ],
    "country": ["SAR", "PAK", "SAR", "PAK", "SAR", "PAK", "SAR", "PAK", "SAR", "PAK"],
    "city": ["Riyadh", "Karachi", "Jeddah", "Lahore", "Dammam", "Islamabad", "Mecca", "Faisalabad", "Medina", "Multan"]
})
print(df)
df.to_csv("data/raw/raw_orders.csv", index=False)