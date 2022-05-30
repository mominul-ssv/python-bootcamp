# method-1
from ecommerce.sales import calc_shipping, calc_tax

# method-2
from ecommerce import sales

# sub-packages
from ecommerce.ecart import cart

print("# =============== method-1 =============== #")
calc_shipping()
calc_tax()

print("# =============== method-2 =============== #")
sales.calc_shipping()
sales.calc_tax()
sales.contact.contact_list()

# sub-packages
cart.calc_cart()

print("# =============== the 'dir' function =============== #")

# print(dir(sales))
print("# ===================== name ===================== #")
print(sales.__name__)

print("# ===================== package ===================== #")
print(sales.__package__)

print("# ===================== file ===================== #")
print(sales.__file__)
