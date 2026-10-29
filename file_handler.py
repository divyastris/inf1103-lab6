import json
import os

from product import Product

FILENAME = "inventory.json"


def load_inventory(inventory):
    """Read inventory.json and add each record to the Inventory as a Product."""
    if os.path.exists(FILENAME):
        print("inventory.json found.")
        with open(FILENAME, "r") as file:
            data = json.load(file)
        for item in data:
            inventory.add_product(Product(item["id"], item["name"],
                                          item["price"], item["stock"]))
        print("Inventory loaded successfully.")
    else:
        print("No inventory.json found. Starting with empty inventory.")


def save_inventory(inventory):
    """Turn each Product back into a dictionary and write them to inventory.json."""
    data = []
    for product in inventory.get_all_products():
        data.append({"id": product.get_product_id(),
                     "name": product.get_name(),
                     "price": product.get_price(),
                     "stock": product.get_stock()})
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully to inventory.json.")