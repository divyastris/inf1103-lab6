from product import Product


class Inventory:
    """Manages a collection of Product objects (Single Responsibility Principle)."""

    def __init__(self):
        self.__products = []

    def add_product(self, product):
        if not isinstance(product, Product):
            raise TypeError("Only Product objects can be added.")
        if self.find_by_id(product.get_product_id()) is not None:
            raise ValueError("A product with ID " + product.get_product_id() + " already exists.")
        self.__products.append(product)

    def find_by_id(self, product_id):
        for product in self.__products:
            if product.get_product_id() == product_id:
                return product
        return None

    def search_product(self, product_id):
        """Return the matching Product, or None if not found."""
        return self.find_by_id(product_id)

    def update_stock(self, product_id, quantity):
        product = self.find_by_id(product_id)
        if product is None:
            return False
        product.update_stock(quantity)  # the Product manages its own stock
        return True

    def get_all_products(self):
        return list(self.__products)  # a copy, so the real list stays private

    def display_all(self):
        print("Current Inventory")
        print("------------------------------------------------")
        for product in self.__products:
            product.display_information()
        print("------------------------------------------------")