from physical_product import PhysicalProduct
from digital_product import DigitalProduct

guitar = PhysicalProduct("P100", "Guitar", 350.0, 5, 3.5)
os_licence = DigitalProduct("D100", "Operating System", 120.0, 40, 4500)

print("--- Section 1 & 2: display_information ---")
guitar.display_information()
os_licence.display_information()