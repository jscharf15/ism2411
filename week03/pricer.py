# Exercise 1: Variables and types

# product = "Notebook"
# unit_price = 4.99
# quantity = 10
# in_stock = True

# print(type(product))
# print(type(unit_price))
# print(type(quantity))
# print(type(in_stock))

# Exercise 2: f-string practice

# total = unit_price * quantity
# print(f"Total: ${total:.2f}")

# print(f"{quantity} units of {product} at ${unit_price:.2f} each = ${unit_price * quantity:.2f}")

# Exercise 3: Input Version

# product_in = input("Product name: ")
# unit_price_in = float(input("Unit price: "))
# quantity_in = int(input("Quantity: "))
# in_stock_in = bool(input("In stock: "))

# print(f"{quantity_in} units of {product_in} at ${unit_price_in:.2f} = ${unit_price_in * quantity_in:,.2f}.")

# Exercise 4: Multi-variable product card

# unit_cost = 3.29
# revenue = unit_price * quantity
# margin = (unit_price - unit_cost) / unit_price * 100

# print(f"Product: {product}\nRevenue: ${revenue:,.2f}\nCost: ${unit_cost:,.2f}\nMargin: {margin:,.2f}%")

# Exercise 5: Type investigation

# type("12")
# type(12)
# type(12.0)
# print(5 + 3)
# print("5" + "3")
# print(5 + "3")
# print("5" + 3)

# "5" + "3" differs from 5 + 3 in that the former is string concatenation, while the latter is numeric addition.