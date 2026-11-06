"""Section 7 tests for Lab 7. Run with:  python -m unittest -v"""
import os
import tempfile
import unittest

from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct
from can_be_shipped import CanBeShipped
from inventory import Inventory
from file_handler import load_inventory, save_inventory


class TestLab7(unittest.TestCase):

    def setUp(self):
        self.guitar = PhysicalProduct("P100", "Guitar", 350.0, 5, 3.5)
        self.os_licence = DigitalProduct("D100", "Operating System", 120.0, 40, 4500)

    # Physical products store their weight
    def test_physical_product_weight(self):
        self.assertEqual(self.guitar.get_weight(), 3.5)
        self.assertEqual(self.guitar.get_name(), "Guitar")  # inherited from Product

    # Digital products store their download size
    def test_digital_product_download_size(self):
        self.assertEqual(self.os_licence.get_download_size(), 4500.0)
        self.assertEqual(self.os_licence.get_stock(), 40)  # inherited from Product

    # Both subclasses implement get_fulfilment_info()
    def test_fulfilment_info(self):
        self.assertIn("physical shipping", self.guitar.get_fulfilment_info())
        self.assertIn("digitally", self.os_licence.get_fulfilment_info())

    # The abstract Product class cannot be instantiated directly
    def test_product_is_abstract(self):
        with self.assertRaises(TypeError):
            Product("X1", "Generic", 1.0, 1)

    # Physical products can calculate shipping costs (different weights)
    def test_shipping_cost(self):
        light = PhysicalProduct("P1", "Mouse", 5.0, 1, 0.1)
        heavy = PhysicalProduct("P2", "Desk", 150.0, 1, 20)
        self.assertEqual(light.calculate_shipping_cost(), 5.20)    # 5 + 2*0.1
        self.assertEqual(self.guitar.calculate_shipping_cost(), 12.00)  # 5 + 2*3.5
        self.assertEqual(heavy.calculate_shipping_cost(), 45.00)   # 5 + 2*20

    # Digital products are not required to implement shipping
    def test_digital_not_shippable(self):
        self.assertIsInstance(self.guitar, CanBeShipped)
        self.assertNotIsInstance(self.os_licence, CanBeShipped)
        self.assertFalse(hasattr(self.os_licence, "calculate_shipping_cost"))

    # Invalid extra attributes are rejected
    def test_invalid_weight_and_size(self):
        with self.assertRaises(ValueError):
            PhysicalProduct("P3", "Bad", 1.0, 1, 0)
        with self.assertRaises(ValueError):
            DigitalProduct("D3", "Bad", 1.0, 1, -5)

    # Inventory operations continue to work
    def test_inventory_operations(self):
        inventory = Inventory()
        inventory.add_product(self.guitar)
        inventory.add_product(self.os_licence)
        self.assertEqual(len(inventory.get_all_products()), 2)
        self.assertIs(inventory.search_product("D100"), self.os_licence)
        self.assertIsNone(inventory.search_product("NOPE"))
        self.assertTrue(inventory.update_stock("P100", 9))
        self.assertEqual(self.guitar.get_stock(), 9)
        with self.assertRaises(ValueError):
            inventory.add_product(PhysicalProduct("P100", "Duplicate", 1.0, 1, 1))

    # JSON saving and loading preserve the correct product types
    def test_json_round_trip(self):
        inventory = Inventory()
        inventory.add_product(self.guitar)
        inventory.add_product(self.os_licence)
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "test_inventory.json")
            save_inventory(inventory, path)

            reloaded = Inventory()  # like restarting the program
            load_inventory(reloaded, path)

        guitar = reloaded.search_product("P100")
        os_licence = reloaded.search_product("D100")
        self.assertIsInstance(guitar, PhysicalProduct)
        self.assertIsInstance(os_licence, DigitalProduct)
        self.assertEqual(guitar.get_weight(), 3.5)
        self.assertEqual(os_licence.get_download_size(), 4500.0)
        self.assertEqual(guitar.get_price(), 350.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
