def add_category(menu, category):
    if category not in menu:
        menu[category] = []
        print(f"Category '{category}' added. ")
    else:
        print(f"Category '{category}' already exists. ")

def add_item(menu, category, item):
    if category in menu:
        if item not in menu[category]:
            menu[category].append(item)
            print(f"Item '{item}' added to '{category}'. ")
        else:
            print(f"Item '{item}' already exists in '{category}', ")
    else: 
        print(f"Category '{category}' does not exist. ")

def remove_item(menu, category, item):
    if category in menu:
        if item in menu[category]:
            menu[category].pop(item)
            print(f"Item '{item}' has been removed from '{category}'. ")
        else:
            print(f"Item '{item}' does not exist in '{category}', ")
    else: 
        print(f"Category '{category}' does not exist. ")

def update_inventory(menu, category, item, price):
    if category in menu:
        if item in category: 
            if price in item:
                menu[category][item].append(price)
    print(f"The price for {item} has been updated to {price} ")


restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

add_category(restaurant_menu, "Beverages")
add_item(restaurant_menu, "Beverages", "Kombucha")
remove_item(restaurant_menu, "Starters", "Bruschetta")
update_inventory(restaurant_menu, "Main Course", "Steak", 17.99)