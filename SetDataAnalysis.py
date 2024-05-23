customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]

def duplicate_cleanup(customer_ids):
    single_ids = set(customer_ids)
    print(f"All duplicates have been removed and the list has been sorted {sorted(single_ids)}")

duplicate_cleanup(customer_ids)