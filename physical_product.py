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
        super().display_information()
        print("    Type: Physical | Weight:", self.__weight, "kg")

    def get_fulfilment_info(self):
        return "Requires physical shipping (" + str(self.__weight) + " kg parcel)."