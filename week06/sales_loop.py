# 1. It's a way to build a result while looping through a list, like a running tally. Three steps: Initialize- Set a starting value before the loop (total = 0). Without it you get an error, and inside the loop it would reset every pass. Update- Change it for each item inside the loop (total = total + n). This is where the answer gets built. Use the result- Print or return it after the loop. Printing inside the loop only shows partial totals.
# 2. The while loop was 2 lines longer because it needed a counter variable and an increment. The for loop handles that automatically. For loop: Shorter, easier to read, fewer mistakes. Best when looping through a known list. While loop: Longer, and forgetting to update the counter causes an infinite loop. But it's more flexible when you don't know how many repeats you need.
# 3. I'd use a list of a stock's daily closing prices for a month, since I'm majoring in finance. List: About 20 to 22 closing prices, one per trading day. Accumulate: A running total of the prices, plus a count of days. Print: The labeled average, like Average closing price: $152.37.

#-----Exercise 1-----
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
count = 0    
count_over_100 = 0
total_over_100 = 0
current_max = sales[0] 
for sale in sales:
    total += sale 
    count += 1 
    if sale > current_max:
        current_max = sale
    if sale > 100:
        count_over_100 += 1
        total_over_100 += sale
print(f"Total: ${total}")
print(f"Count: {count}")
print(f"Average: ${total / count:.2f}")
print(f"Largest sale: ${current_max}")
print(f"Sales over $100: {count_over_100}")
print(f"Total of those sales: ${total_over_100}")

#-----Exercise 2-----
# count += 1
# print(f"Count: {count}")
# print(f"Average: ${total / count}")

#-----Exercise 3-----
# current_max = sales[0]
# if sale > current_max:
#   current_max = sale
# print(f"Largest sale: ${current_max}")

#-----Exercise 4-----
# sales_over_100 = 0
# total_over_100 = 0
# if sale > 100:
#   sales_over_100 += 1
#   total_over_100 += sale
# print(f"Sales over $100: {sales_over_100}")
# print(f"Total of those sales: ${total_over_100}")

#-----Exercise 5-----
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale > 400:
        print(f"Alert: outlier found - ${sale}. Stopping.")
        break
    if sale <= 100:
        continue
    print(f"${sale}")

#-----Exercise 6-----
sales = [120, 80, 250, 175, 90, 410, 60, 215]
total = 0
i = 0           
while i < len(sales):
    total += sales[i]
    i += 1
print(f"Total (while loop): ${total}")
# I would use the for loop in production. It is shorter (4 vs. 6) and has no index to manage, so it can't turn into an infinite loop if I forget i += 1.

#-----Exercise 7-----
sales = [120, 80, 250, 175, 90, 410, 60, 215]
for sale in sales:
    if sale >= 200:
        discount = 0.10
    elif sale >= 100:
        discount = 0.05
    else:
        discount = 0
    discounted_price = sale * (1 - discount)
    
    print(f"${sale} -> {discount*100:.0f}% discount -> ${discounted_price:.2f}") 