from models import Item
from storage import load_inventory, save_inventory


# Adds a new item to the inventory
def add_item(item_id, name, quantity, price):
    items = load_inventory()

    # Check if item ID already exists
    for item in items:
        if item.item_id == item_id:
            return False

    # Add new item to list
    items.append(Item(item_id, name, quantity, price))
    save_inventory(items)
    return True


# Returns all items in the inventory
def get_all_items():
    return load_inventory()


# Searches for an item by ID
def find_item(item_id):
    items = load_inventory()
    for item in items:
        if item.item_id == item_id:
            return item
    return None


# Updates quantity and price of an item
def update_item(item_id, quantity, price):
    items = load_inventory()
    for item in items:
        if item.item_id == item_id:
            item.quantity = quantity
            item.price = price
            save_inventory(items)
            return True
    return False


# Deletes an item from the inventory
def delete_item(item_id):
    items = load_inventory()
    new_items = []

    # Keep all items except the one to delete
    for item in items:
        if item.item_id != item_id:
            new_items.append(item)

    save_inventory(new_items)
