import json
import os

from physical_product import PhysicalProduct
from digital_product import DigitalProduct

FILENAME = "inventory.json"


def create_product_from_dict(item):
    """Use the saved 'type' identifier to rebuild the correct subclass."""
    product_type = item.get("type")
    if product_type == "physical":
        return PhysicalProduct(item["id"], item["name"], item["price"],
                               item["stock"], item["weight"])
    elif product_type == "digital":
        return DigitalProduct(item["id"], item["name"], item["price"],
                              item["stock"], item["download_size"])
    else:
        raise ValueError("Unknown product type: " + str(product_type))


def load_inventory(inventory, filename=FILENAME):
    """Read the JSON file and add each record to the Inventory as the right product type."""
    if os.path.exists(filename):
        print(filename, "found.")
        with open(filename, "r") as file:
            data = json.load(file)
        for item in data:
            try:
                inventory.add_product(create_product_from_dict(item))
            except (ValueError, KeyError) as error:
                print("Skipped a record (" + str(item.get("id")) + "):", error)
        print("Inventory loaded successfully.")
    else:
        print("No", filename, "found. Starting with empty inventory.")


def save_inventory(inventory, filename=FILENAME):
    """Ask each Product for its own dictionary, then write them all to the JSON file."""
    data = []
    for product in inventory.get_all_products():
        data.append(product.to_dict())  # each product knows its own fields + type
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)
    print("Inventory saved successfully to", filename + ".")