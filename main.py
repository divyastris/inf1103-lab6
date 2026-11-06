from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from file_handler import load_inventory, save_inventory


def add_product_menu(inventory):
    print("Product type:")
    print("  1. Physical product")
    print("  2. Digital product")
    product_type = input("Choose type (1 or 2): ")
    if product_type not in ("1", "2"):
        print("Invalid product type.")
        return

    new_id = input("Product ID: ")
    new_name = input("Product Name: ")
    try:
        new_price = float(input("Price: "))
        new_stock = int(input("Stock Quantity: "))
        if product_type == "1":
            weight = float(input("Weight (kg): "))
            product = PhysicalProduct(new_id, new_name, new_price, new_stock, weight)
        else:
            download_size = float(input("Download size (MB): "))
            product = DigitalProduct(new_id, new_name, new_price, new_stock, download_size)
        inventory.add_product(product)
        print("Product added successfully!")
    except ValueError as error:
        print("Could not add product:", error)


def update_stock_menu(inventory):
    search_id = input("Enter Product ID: ")
    product = inventory.search_product(search_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found:")
    print("Name:", product.get_name())
    print("Current Stock:", product.get_stock())
    try:
        new_stock = int(input("New Stock Quantity: "))
        inventory.update_stock(search_id, new_stock)
        print("Stock updated successfully!")
    except ValueError as error:
        print("Could not update stock:", error)


def search_product_menu(inventory):
    search_id = input("Enter Product ID: ")
    product = inventory.search_product(search_id)
    if product is None:
        print("Product not found.")
        return
    print("Product Found")
    print("------------------------------------------------")
    product.display_information()
    print("Fulfilment:", product.get_fulfilment_info())
    # Only objects that signed the CanBeShipped contract have a shipping cost
    if isinstance(product, CanBeShipped):
        print("Shipping cost: $" + format(product.calculate_shipping_cost(), ".2f"))
    print("------------------------------------------------")


# ---- Main program starts here ----
if __name__ == "__main__":
    print("=" * 40)
    print("INVENTORY MANAGEMENT SYSTEM")
    print("=" * 40)

    inventory = Inventory()
    load_inventory(inventory)

    while True:
        print("----------- MENU -----------")
        print("1. Display All Products")
        print("2. Add Product")
        print("3. Update Stock")
        print("4. Search Product")
        print("5. Save Inventory")
        print("6. Exit")
        print("----------------------------")
        choice = input("Enter option: ")

        if choice == "1":
            inventory.display_all()
        elif choice == "2":
            add_product_menu(inventory)
        elif choice == "3":
            update_stock_menu(inventory)
        elif choice == "4":
            search_product_menu(inventory)
        elif choice == "5":
            save_inventory(inventory)
        elif choice == "6":
            save_inventory(inventory)
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")