"""CP-1404 - prac_03"""

# Task 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)  # or out_file.write(name)
out_file.close()

# Task 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print("Your name is", name)
in_file.close()

# Task 3 - Sum of the first two numbers
in_file = open("number.txt", "r")
number1 = int(in_file.readline())
number2 = int(in_file.readline())
print("The sum of the first two numbers is:", number1 + number2)
in_file.close()

# Task 3 extended - Sum of all numbers
total_all_numbers = 0
in_file = open("number.txt", "r")
for line in in_file:
    number = int(line)
    total_all_numbers += number
in_file.close()

print("The total for all numbers is:", total_all_numbers)
