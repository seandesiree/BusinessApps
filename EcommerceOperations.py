import re

def analysis_descriptions(descriptions):
    electronics_pattern = r"\b(smartphone)\b"
    apparel_pattern = r"\b(t-shirt)\b"
    home_pattern = r"\b(kitchen)\b"

    try:
        if re.search(electronics_pattern, descriptions, re.IGNORECASE):
            return "Electronics"
        elif re.search(apparel_pattern, descriptions, re.IGNORECASE):
            return "Apparel"
        elif re.search(home_pattern, descriptions, re.IGNORECASE):
            return "Home"
        else:
            return "N/A"
        
    except Exception as e:
        print(f"Error analyzing descriptions: {e}")
        return "N/A"

def organize_descriptions(descriptions):
    organize_products = {"Electronics": [], "Apparel": [], "Home": []}
    for item in descriptions:
        try:
            product = analysis_descriptions(item)
            organize_products[product].append(item)
        except Exception as e:
            print(f"Keyword is not in descriptions. ")
    return organize_products


descriptions = [
    "Smartphone with 6-inch screen and 128GB memory",
    "Cotton t-shirt in medium size",
    "Stainless steel kitchen knife set"
]

product_by_description = organize_descriptions(descriptions)
for product, text in product_by_description.items():
    print(f"{product}, {text}")

