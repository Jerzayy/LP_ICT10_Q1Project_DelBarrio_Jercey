from pyscript import display

# Restaurant Ordering system using Python Display

# String Data Type
restaurant_name = "DunDun's shop"
owner_name = "JC Del Barrio"

# Integer Data Type
year_since = 2025

# Float Data Type
tax_rate = 0.08

# Boolean Data Type
has_delivery = True
is_dine_in = True
is_takeaway = False

# List Data Type
product_names = ["Fish ball", "Kwek Kwek", "Kikiam", "Turon", "Buko juice"]

# Tuple Data Type
business_hours = ("9:00 AM", "7:00 PM")

# Dictionary Data Type
menu = {
    "Fish ball": 120.00,
    "Kwek Kwek": 200.50,
    "Kikiam": 99.00,
    "Turon": 80.00,
    "Buko juice": 20.50,
}

# Set Data Type
common_allergens = {"nuts", "gluten", "dairy", "soy"}

# Display the restaurant information
display(restaurant_name, target="name1")
display(f"Owner: {owner_name}", target="owner")
display(f"Since: {year_since}", target="since")   # fixed
display("Menu Pricelist", target="heading1")

# Display menu items
display(product_names[0], target="prod1")
display(f"₱{menu['Fish ball']}", target="price1")

display(product_names[1], target="prod2")
display(f"₱{menu['Kwek Kwek']}", target="price2")

display(product_names[2], target="prod3")
display(f"₱{menu['Kikiam']}", target="price3")

display(product_names[3], target="prod4")
display(f"₱{menu['Turon']}", target="price4")

display(product_names[4], target="prod5")
display(f"₱{menu['Buko juice']}", target="price5")

# Additional information
display(f"Open: {business_hours[0]} - {business_hours[1]}", target="openingHours")  # fixed

# Display order type 
display(f"Dine-In Available: {is_dine_in}", target="orderType")  # fixed
