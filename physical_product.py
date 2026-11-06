from product import Product


class PhysicalProduct(Product):
    """A PhysicalProduct IS-A Product (inheritance)."""

    def __init__(self, product_id, name, price, stock, weight):
        super().__init__(product_id, name, price, stock)  # reuse Product's constructor
        weight = float(weight)
        if weight <= 0:
            raise ValueError("Weight must be more than 0 kg.")
        self.__weight = weight

    def get_weight(self):
        return self.__weight

    def display_information(self):
        print("ID:", self.get_product_id(), "| Name:", self.get_name(),
              "| Price: $" + str(self.get_price()), "| Stock:", self.get_stock())
        print("    Type: Physical | Weight:", self.__weight, "kg")