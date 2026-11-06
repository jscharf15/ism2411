# -----Exercise 1-----

total = float(input("Enter cart total: $"))

# Add your if/elif/else here
if total >= 500:
    discount = 0.15
elif total >= 200:
    discount = 0.10
elif total >= 100:
    discount = 0.05
else:
    discount = 0

# -----Exercise 3------

region = "South"
extra_discount = 0
if region == "South" and total >= 100:
    extra_discount = 0.02
    print("Region bonus applied: additional 2% off")

final_discount = discount + extra_discount
final_price = total * (1-final_discount)

print(f"Discount: {final_discount:.0%}") # Gives whole percentage not the rate
print(f"Final price: ${final_price:,.2f}") # give final at 2 decimals with commas

# -----Exercise 2-----
if final_price > 1000:
    status = "manager_approval_required"
else:
    status = "auto_approved"

print(f"Status: {status}")

# -----Exercise 4-----

customer_type = "wholesale"
# if region == "South":
#     if total >= 100:
#         if customer_type == "wholesale":
#             extra_discount = 0.03
if region == "South" and total >= 100 and customer_type == "wholesale":
    extra_discount = 0.03
           
# Flat version — easier to read since both conditions are right there in one line, and easier to test since there are fewer cases to check.

# -----Exercise 5-----
amount = -50

if amount <= 0:
    print("SUSPICIOUS")
elif amount < 10000:
    print("NORMAL")
else:
    print("LARGE - REVIEW REQUIRED") 

# -----Exercise 6-----

total_spent_this_year = 2500
orders_this_year = 6
has_outstanding_balance = False


qualifies_by_spending = total_spent_this_year > 2000
qualifies_by_orders = orders_this_year > 10

vip_upgrade = (qualifies_by_spending or qualifies_by_orders) and not has_outstanding_balance

print(f"VIP upgrade: {vip_upgrade}")