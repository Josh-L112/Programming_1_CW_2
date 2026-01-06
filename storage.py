import json
import os
from models import Item

# File path for storing inventory data
DATA_FILE = "data/inventory.json"


# Loads inventory data from the JSON file
def load_inventory():
    # If file does not exist, return an empty list
    if not os.path.exists(DATA_FILE):
        return []

    # Open and read JSON file
    with open(DATA_FILE, "r") as file:
        data = json.load(file)

    items = []
    # Convert each dictionary into an Item object
    for item in data:
        items.append(Item(
            item["item_id"],
            item["name"],
            item["quantity"],
            item["price"]
        ))
    return items


# Saves inventory data to the JSON file
def save_inventory(items):
    with open(DATA_FILE, "w") as file:
        # Convert Item objects to dictionaries before saving
        json.dump([item.__dict__ for item in items], file, indent=4)
