try:
    amount = "100"
    total = amount + 50
    print(f"Total amount: {total}")
except TypeError:
    try:
        print("EXCEPTION ====== A type error occurred.")
        total = float(amount) + 50
        print(f"Total amount after conversion: {total}")
    except Exception as e:
        print(f"An error occurred: {e}")