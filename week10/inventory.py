# Reflection
# 1. The most surprising thing about lists was that they can be changed while
#    tuples cannot. In Exercise 4, I could append(), remove(), and sort() the list
#    freely, but in Exercise 5, trying to change coords[0] raised a TypeError.
#    That showed me why a fixed pair like coordinates works better as a tuple.
# 2. At my summer food program job, we made and delivered lunches for programs in our area. 
#    Every day, lunch counts, milk inventory, and our mileage sheet changed, and I calculated 
#    the mileage by hand. With Python lists, I could use sum() for the daily totals and a loop 
#    with an if statement to flag low inventory, saving time compared to redoing it in Excel.

print("----- Exercise 1: Build the list -----")

inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

print("----- Exercise 2: Index practice -----")
print(inventory[0]) # first item
print(inventory[-1]) # last item
middle = len(inventory) // 2 # calculate the index of the middle
print(inventory[middle]) # middle item

print("----- Exercise 3: Slicing Practice -----")
print(inventory[:3]) # first three items
print(inventory[-2:]) # last two items
print(inventory[::2]) # every other item

print("----- Exercise 4: Modifying the list -----")
inventory.append("envelope")
print(inventory) # output: ['pen', 'notebook', 'stapler', 'tape', 'marker', 'envelope']

inventory.remove("tape")
print(inventory) # output: ['pen', 'notebook', 'stapler', 'marker', 'envelope']

inventory.sort()
print(inventory)

print("----- Exercise 5: Tuple comparison -----")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as error:
    print("TypeError caught:", error)
    print("Tuples protect coordinates: a location should never change by accident.")

print(coords)

print("----- Exercise 6: Average of a list of sales -----")
sales = [100, 250, 75, 480, 200]
total = sum(sales)
count = len(sales)
average = total / count

print(f"Total: {total}")
print(f"Count: {count}")
print(f"Average: {average}")
print(f"Best: {max(sales)}")
print(f"Worst: {min(sales)}")

print("----- Exercise 7: Accumulator pattern -----")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.9, 2))

print(f"Original prices: {prices}")
print(f"Discounted prices: {discounted}")

print("----- Exercise 8: Filter above threshold -----")
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []
for amount in sales:
    if amount > 300:
        high_sales.append(amount)

print(f"High sales: {high_sales}")
print(f"Count: {len(high_sales)}")
print(f"Average: {sum(high_sales) / len(high_sales):.2f}")