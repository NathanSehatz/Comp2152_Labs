inventory = {
    "Laptop": (999.99, 5),
    "Mouse": (29.99, 15),
    "Keyboard": (79.99, 10),
    "Monitor": (299.99, 8)
}

print("=== Current Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {quantity}")

print()

electronics = {"Laptop", "Monitor"}
accessories = {"Mouse", "Keyboard"}

all_products = electronics | accessories
print("All product categories:", all_products)
print()

price_list = []
for product, (price, quantity) in inventory.items():
    price_list.append(price)

print("Price list:", price_list)

price_list.sort()
print("Sorted prices:", price_list)
print(f"Lowest price: ${price_list[0]:.2f}")
print(f"Highest price: ${price_list[-1]:.2f}")
print()

inventory["Headphones"] = (49.99, 20)

mouse_price = inventory["Mouse"][0]
inventory["Mouse"] = (mouse_price, 12)

del inventory["Monitor"]

print("=== Final Inventory ===")
for product, (price, quantity) in inventory.items():
    print(f"{product} - Price: ${price:.2f}, Quantity: {quantity}")
