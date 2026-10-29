from product import Product
from inventory import Inventory
from file_handler import load_inventory, save_inventory


def add_product_menu(inventory):
    new_id = input("Product ID: ")
    new_name = input("Product Name: ")
    try:
        new_price = float(input("Price: "))
        new_stock = int(input("Stock Quantity: "))
        inventory.add_product(Product(new_id, new_name, new_price, new_stock))
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
    print("ID:", product.get_product_id())
    print("Name:", product.get_name())
    print("Price: $" + str(product.get_price()))
    print("Stock:", product.get_stock())
    print("------------------------------------------------")


# ---- Main program starts here ----
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