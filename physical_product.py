from product import Product
from can_be_shipped import CanBeShipped

class PhysicalProduct(Product, CanBeShipped):
    """A PhysicalProduct IS-A Product and CAN-BE-SHIPPED."""

    BASE_SHIPPING_FEE = 5.00   # flat fee for every parcel
    RATE_PER_KG = 2.00         # extra charge for each kg

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

    def calculate_shipping_cost(self):
        """Simple rule: $5.00 flat fee + $2.00 per kg."""
        return round(self.BASE_SHIPPING_FEE + self.RATE_PER_KG * self.__weight, 2)

    def to_dict(self):
        data = super().to_dict()                # parent gives the common fields
        data["type"] = "physical"               # type identifier for loading
        data["weight"] = self.__weight
        return data