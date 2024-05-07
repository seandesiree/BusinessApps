import copy

weekly_sales = {
    "Week 1": {"Electronics": 12000, "Clothing": 5000, "Groceries": 7000},
    "Week 2": {"Electronics": 15000, "Clothing": 6000, "Groceries": 8000}
}

weekly_sales_copy = copy.deepcopy(weekly_sales)

if "Week 2" in weekly_sales_copy:
    weekly_sales_copy["Week 2"]["Electronics"] = 18000
else:
    print("Week 2 not found in the copied data.")


print("Original Weekly Sales Data:")
for week, sales_data in weekly_sales.items():
    print(f"{week}:")
    for category, amount in sales_data.items():
        print(f"  - {category}: {amount}")

print("\nCopied Weekly Sales Data with Updated Electronics Sales in Week 2:")
for week, sales_data in weekly_sales_copy.items():
    print(f"{week}:")
    for category, amount in sales_data.items():
        print(f"  - {category}: {amount}")

