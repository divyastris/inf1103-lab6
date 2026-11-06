from abc import ABC, abstractmethod

class Product(ABC):
    """Represents and manages ONE product (Single Responsibility Principle)."""

    def __init__(self, product_id, name, price, stock):
        self.__product_id = product_id
        self.__name = name
        self.__price = float(price)
        self.__stock = 0
        self.update_stock(stock)  # reuse the validation in update_stock

    # Public getters: external code can read, but not change, the data directly
    def get_product_id(self):
        return self.__product_id

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_stock(self):
        return self.__stock

    def update_stock(self, quantity):
        """Set the stock level. The Product decides what is acceptable."""
        if not isinstance(quantity, int) or quantity < 0:
            raise ValueError("Stock must be a whole number that is 0 or more.")
        self.__stock = quantity

    def display_information(self):
        print("ID:", self.__product_id, "| Name:", self.__name,
              "| Price: $" + str(self.__price), "| Stock:", self.__stock)

    def to_dict(self):
        """Return the common product data as a dictionary (used for saving to JSON)."""
        return {"id": self.__product_id,
                "name": self.__name,
                "price": self.__price,
                "stock": self.__stock}

    @abstractmethod
    def get_fulfilment_info(self):
        """Return how this product reaches the customer.
        No implementation here - every child class MUST provide its own."""
        pass