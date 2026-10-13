# Self-Assessment
# 1. The first bug I spotted was the missing colon on line 10. I found it from the traceback, which pointed to the exact line and said it expected a colon. That tells me my instinct is to rely on error messages first, which works for crashes.
# 2. What it does is take a number (price) and tier (string) and returns the price after the discount that matches the tier, depending on what tier was inputted. It returns a number, not a printed message. A colleague could use it without reading the body, as long as a docstring explained what it does and expects. 
# 3. AI disclosure: I used Claude to explain what the errors meant in Exercise 5. I also had a question about how to effectively use print() tracing. Claude helped build my understanding to a level where I could actually understand the question and build an informed answer. 

# -----Exercise 1-----

def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax on $100 at 7%: ${tax1:.2f}") # 7.00
print(f"Tax on $250 at 8%: ${tax2:.2f}") # 20.00

# -----Exercise 2-----

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200
tiers = ["gold", "silver", "bronze", "none"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# -----Exercise 3-----

# Manual -- As done in class --
# discounted = apply_discount(200, "gold")
# tax = calculate_tax(discounted, 0.07)
# after_tax = discounted + tax
# print(f"After gold discount: ${discounted:.2f}")
# print(f"After Tax: ${after_tax:.2f}")

# Function
def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

discounted = apply_discount(200, "gold")
after_tax = discounted + calculate_tax(discounted, 0.07)

print(f"After gold discount: ${discounted:.2f}")
print(f"After tax: ${after_tax:.2f}")
print(f'final_price(200, "gold", 0.07) = ${final_price(200, "gold", 0.07):.2f}')

# -----Exercise 4-----

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")

# -----Exercise 5-----

# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale
print(f"Total: ${total}")

count = 0
for sale in sales:
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):
    print(sales[i])
    i += 1

# total = 0
# for sale in sales:
#     total = sale
#     print("sale:", sale, "total:", total)

# Line 10 was missing ":" at the end of the line. This is a Syntax Error because there is a "for" loop. If there is a for or while loop, there must be a colon at the end of the line or Python can't read it. 
# Line 15 had "<=" when it should have just been "<" because when i reached 5 it tried sales[5], which doesn't exist (IndexError), so I changed it to i < len(sales) because 5 is not less than 5, so it stops.
# Line 6 had an error as well that did not get flagged. total = sale makes no sense. Python replaced the total on every pass, so it ended with the final sale (90) as the total, not the total of the sales. So I had to change it to total += sale to add the sales. 

# -----Exercise 6-----

x = 100   # global variable

def double_it():
    x = 999   # local variable — different from global x!
    return x * 2

print(x)           # Prediction: 100
print(double_it()) # Prediction: 1998
print(x)           # Prediction: 100
# Scope: Scope is the area of your code where a specific variable can be seen and used.
# 1st print: 100, the global x. Python uses the global x because there is no local x in the main body of the code.
# 2nd print: 1998, because the function uses its own local x (999) and doubles it.
# 3rd print: 100, because the global x was never changed by the function.