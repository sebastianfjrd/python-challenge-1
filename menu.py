menu = {
    "Snacks": {
        "Cookie": 0.99,
        "Banana": 0.69,
        "Apple": 0.49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

order_list = []

def print_menu(menu_category):
    print("Item # | Item name                | Price")
    print("-------|--------------------------|-------")
    i = 1
    menu_items = {}
    for key, value in menu_category.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                item_name = f"{key} - {sub_key}"
                item_price = sub_value
                print(f"{i:<6} | {item_name:<25} | ${item_price:.2f}")
                menu_items[i] = {"Item name": item_name, "Price": item_price}
                i += 1
        else:
            item_name = key
            item_price = value
            print(f"{i:<6} | {item_name:<25} | ${item_price:.2f}")
            menu_items[i] = {"Item name": item_name, "Price": item_price}
            i += 1
    return menu_items

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print("Invalid input, please try again.")

def get_valid_number(prompt, default=None):
    user_input = input(prompt)
    if user_input.isdigit():
        return int(user_input)
    elif default is not None:
        return default
    else:
        print("Invalid input, defaulting to 1.")
        return 1

print("Welcome to the Awesome Variety Food Truck.")
place_order = True
while place_order:
    print("From which menu would you like to order?")
    for i, key in enumerate(menu.keys(), start=1):
        print(f"{i}: {key}")
    
    menu_category_num = get_valid_number("Type menu number to view or q to quit: ")
    if menu_category_num in range(1, len(menu) + 1):
        menu_category_name = list(menu.keys())[menu_category_num - 1]
        print(f"You selected {menu_category_name}")
        menu_items = print_menu(menu[menu_category_name])
        
        menu_item_num = get_valid_number("Please indicate the Item # you would like to order: ")
        if menu_item_num in menu_items:
            item_name = menu_items[menu_item_num]['Item name']
            item_price = menu_items[menu_item_num]['Price']
            quantity = get_valid_number(f"How many {item_name} would you like to order? ", default=1)
            
            order_list.append({"Item name": item_name, "Price": item_price, "Quantity": quantity})
        else:
            print("You didn't enter a valid item number.")
    else:
        print(f"{menu_category_num} was not a valid menu option.")
    
    keep_ordering = get_valid_input("Would you like to keep ordering? (Y)es or (N)o ", valid_options=['y', 'n'])
    match keep_ordering:
        case 'y':
            place_order = True
        case 'n':
            place_order = False
            print("Thank you for your order!")
        case _:
            print("Invalid response, please try again.")

print("This is what we are preparing for you.\n")
print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

total_cost = sum(order['Price'] * order['Quantity'] for order in order_list)
for order in order_list:
    item_name = order["Item name"]
    price = order["Price"]
    quantity = order["Quantity"]
    num_item_spaces = 26 - len(item_name)
    item_spaces = " " * num_item_spaces
    print(f"{item_name}{item_spaces} | ${price:<6.2f} | {quantity}")

print("--------------------------|--------|----------")
print(f"Total Cost: ${total_cost:.2f}")
