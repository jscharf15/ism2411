# Exercise 1
price = 50
quantity = 12
revenue = price * quantity
print(f"Revenue: ${revenue:.2f}")

# Exercise 2
cost = 32
price = 50
margin = (price - cost) / price # We want a float; the underlying variable NEVER changes
print(f"Margin: {margin:.1%}") # Percentage format


# Exercise 3

margin_a = .36
margin_b = .25

print(f"Margin A: {margin_a}")
print(f"Margin B: {margin_b}")

product_a_wins = margin_a > margin_b
print(f"Product A wins: {product_a_wins}")

# Exercise 4
price = 150
margin = 0.35
is_premium = price > 100
good_margin = margin > 0.3
use_product = is_premium and good_margin

print(price)
print(margin)
print(f"Is Premium = {is_premium}")
print(f"Good Margin = {good_margin}")
print(f"Use Product = {use_product}")

# Exercise 5
print(17 / 5) # answer = 3.4. It divides the first number by the second number and returns a float.
print(17 // 5) # answer = 3. It divides the first number by the second number and returns a rounded integer.
print(17 % 5) # answer = 2. It divides the first number by the second number and returns the remainder of the division.

# Exercise 6

# Stage 1: Inputs
product = input("Enter product name: ") # str
price = float(input("Enter product price: ")) # float
cost = float(input("Enter product cost: ")) # float
quantity = int(input("Enter quantity sold: ")) # int
discount = float(input("Enter discount percentage: ")) # float

# Stage 2: Calculations
revenue = price * quantity
discounted_revenue = revenue * (1 - discount) 
gross_margin = (price - cost) / price
net_profit = discounted_revenue - (cost * quantity)

# Stage 3: Outputs
print(f"Product: {product}")
print(f"Revenue: ${revenue:,.2f}")
print(f"Net Revenue: ${discounted_revenue:,.2f}")
print(f"Margin: {gross_margin:.1%}")
print(f"Profit: ${net_profit:,.2f}")

# Exercise 7
BOX_SIZE = 24 # CONSTANT DO NOT TOUCH
items_ordered = int(input("Number of items ordered: "))
full_boxes = items_ordered // BOX_SIZE # floor division
loose_items = items_ordered % BOX_SIZE # modulus operator
exact_fit = loose_items == 0

print(f"Full boxes: {full_boxes}")
print(f"Loose items: {loose_items}")
print(f"Exact fit: {exact_fit}")

