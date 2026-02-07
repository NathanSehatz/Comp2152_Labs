cart = ["apple", "banana", "milk", "bread", "apple", "eggs"]

print("Number of apples:", cart.count("apple"))
print("Position of milk:", cart.index("milk"))

cart.remove("apple")          # removes the first "apple"
removed_item = cart.pop()     # removes last item

print("Removed item using pop:", removed_item)
print("Is banana in cart?", "banana" in cart)
print("Final cart:", cart)
