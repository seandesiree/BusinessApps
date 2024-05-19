catalog1 = (("Laptop", 1000), ("Camera", 500))
catalog2 = (("Smartphone", 800), ("Tablet", 450))

def product_catalog():
    merged = catalog1 + catalog2
    print(merged)

product_catalog()