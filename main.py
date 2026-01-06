import inventory
from utils import get_int, get_float, print_items

# Main program loop
while True:
    # Display menu options
    print("\nInventory Management System")
    print("1. Add item")
    print("2. View items")
    print("3. Search item")
    print("4. Update item")
    print("5. Delete item")
    print("6. Exit")

    choice = input("Choose an option: ")

    # Add item
    if choice == "1":
        item_id = input("Item ID: ")
        name = input("Item name: ")
        quantity = get_int("Quantity: ")
        price = get_float("Price: ")

        if inventory.add_item(item_id, name, quantity, price):
            print("Item added.")
        else:
            print("Item already exists.")

    # View all items
    elif choice == "2":
        print_items(inventory.get_all_items())

    # Search for an item
    elif choice == "3":
        item_id = input("Item ID: ")
        item = inventory.find_item(item_id)
        if item:
            print_items([item])
        else:
            print("Item not found.")

    # Update an item
    elif choice == "4":
        item_id = input("Item ID: ")
        quantity = get_int("New quantity: ")
        price = get_float("New price: ")
        if inventory.update_item(item_id, quantity, price):
            print("Item updated.")
        else:
            print("Item not found.")

    # Delete an item
    elif choice == "5":
        item_id = input("Item ID: ")
        inventory.delete_item(item_id)
        print("Item deleted.")

    # Exit program
    elif choice == "6":
        print("Goodbye.")
        break

    # Invalid option
    else:
        print("Invalid option.")
