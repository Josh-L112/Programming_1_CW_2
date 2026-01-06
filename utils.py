# Gets a valid integer from the user
def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except:
            print("Please enter a number.")


# Gets a valid float from the user
def get_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except:
            print("Please enter a valid price.")


# Prints inventory items in a simple format
def print_items(items):
    if len(items) == 0:
        print("No items found.")
        return

    print("\nID | Name | Quantity | Price")
    print("-----------------------------")
    for item in items:
        print(item.item_id, "|", item.name, "|", item.quantity, "| £", item.price)
