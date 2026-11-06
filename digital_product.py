from product import Product


class DigitalProduct(Product):
    """A DigitalProduct IS-A Product."""

    def __init__(self, product_id, name, price, stock, download_size):
        super().__init__(product_id, name, price, stock)  # reuse Product's constructor
        download_size = float(download_size)
        if download_size <= 0:
            raise ValueError("Download size must be more than 0 MB.")
        self.__download_size = download_size

    def get_download_size(self):
        return self.__download_size

    def display_information(self):
        super().display_information()
        print("    Type: Digital | Download size:", self.__download_size, "MB")