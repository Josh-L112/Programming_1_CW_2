# Item class used to store inventory item details
class Item:
    def __init__(self, item_id, name, quantity, price):
        # Unique ID for the item
        self.item_id = item_id
        # Name of the item
        self.name = name
        # Quantity in stock
        self.quantity = quantity
        # Price of the item
        self.price = price
