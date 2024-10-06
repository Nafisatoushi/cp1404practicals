"""CP-1404 - Prac-03"""

import random

print(random.randint(5, 20))  # line 1
# What did you see on line 1?
# Answer: The output is a random integer between 5 and 20 (inclusive).

# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest: 5, Largest: 20

print(random.randrange(3, 10, 2))  # line 2
# What did you see on line 2?
# Answer: The output is a random odd integer between 3 and 9 because of the step 2.

# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest: 3, Largest: 9

# Could line 2 have produced a 4?
# Answer: No, because the step is 2, and 4 is not an odd number.

print(random.uniform(2.5, 5.5))  # line 3
# What did you see on line 3?
# Answer: The output is a random floating-point number between 2.5 and 5.5.

# What was the smallest number you could have seen, what was the largest?
# Answer: Smallest: 2.5, Largest: 5.5


# Write code to produce a random number between 1 and 100 inclusive.
random_number = random.randint(1, 100)
print(random_number)
