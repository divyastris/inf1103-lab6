from product import Product
from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P100", "Guitar", 350.0, 5, 3.5)
os_licence = DigitalProduct("D100", "Operating System", 120.0, 40, 4500)

print("--- Section 1 & 2: display_information ---")
guitar.display_information()
os_licence.display_information()

print("--- Section 3: get_fulfilment_info ---")
print(guitar.get_fulfilment_info())
print(os_licence.get_fulfilment_info())

print("--- Section 3.3: try to create a plain Product ---")
try:
    Product("X1", "Generic", 1.0, 1)
except TypeError as error:
    print("Cannot create Product directly:", error)

print("--- Section 4: shipping cost for different weights ---")
for weight in [0.1, 3.5, 20]:
    item = PhysicalProduct("P999", "Test box", 10.0, 1, weight)
    print(weight, "kg -> shipping $" + format(item.calculate_shipping_cost(), ".2f"))