"""
CP1404 - prac_01
Shop calculator program to determine total price
"""

total = 0
number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    price = float(input("Price of item: "))
    total += price

if total > 100:
    total *= 0.9  # 10% discount

print("Total price for ", number_of_items, " items is $", total, sep='')

print(f"Total price for {number_of_items} items is ${total:.2f}")
