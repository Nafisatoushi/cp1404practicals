"""CP-1404 - prac_03"""

# Task 1
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)  # or out_file.write(name)
out_file.close()

# Task 2
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()