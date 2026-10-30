# Self Assessment
# 1. The most surprising thing about lists was that they can be changed while
#    tuples cannot. In Exercise 4, I could append(), remove(), and sort() the list
#    freely, but in Exercise 5, trying to change coords[0] raised a TypeError.
#    That showed me why a fixed pair like coordinates works better as a tuple.
# 2. At my summer food program job, we made and delivered lunches for programs in our area. 
#    Every day, lunch counts, milk inventory, and our mileage sheet changed, and I calculated 
#    the mileage by hand. With Python lists, I could use sum() for the daily totals and a loop 
#    with an if statement to flag low inventory, saving time compared to redoing it in Excel.

# ----- Exercise 1 -----
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))

# ----- Exercise 2 -----
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])

# ---- Exercise 3 -----
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])

# ---- Exercise 4 -----
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)

# ---- Exercise 5 -----
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError as e:
    print("TypeError caught:", e)
    print("Tuples are useful for coordinates because they are immutable. "
          "A latitude/longitude pair describes a fixed location, so it "
          "shouldn't be changed by accident.")

print(coords)

# ---- Exercise 6 -----
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print("Total:", total)
print("Count:", count)
print("Average:", average)
print("Best:", max(sales))
print("Worst:", min(sales))

# ---- Exercise 7 -----
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted = []

for price in prices:
    discounted.append(round(price * 0.9, 2))

print(prices)
print(discounted)

# --- Exercise 8 -----
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print("Count:", len(high_sales))
print("Avg:", round(sum(high_sales) / len(high_sales), 2))
