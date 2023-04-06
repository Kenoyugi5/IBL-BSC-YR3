# This code sets the variable `number_of_time` to 0 and then enters a while loop that will execute the
# code block as long as `number_of_time` is less than 3. The code block simply prints the string
# "Hello, world" and then increments `number_of_time` by 1. This loop will execute three times,
# printing "Hello, world" each time.
"""number_of_time = 0
while number_of_time < 3:
    print("Hello, world")
      number_of_time += 1"""

# A for loop that iterates over the list [0, 1, 2] and assigns each value to the variable
# `number_of_time`. Then it prints the string "Hello, world" for each value in the list. This loop
# will execute three times, printing "Hello, world" each time.
"""for number_of_time in [0, 1, 2]:
    print("Hello, world")"""

# A for loop that iterates over the range of numbers from 0 to 2 (inclusive) and assigns each value to
# the variable `number_of_time`. Then it prints the string "Hello, World" for each value in the range.
# This loop will execute three times, printing "Hello, World" each time.
"""for number_of_time in range(3):
    print("Hello, World")"""

# A for loop that iterates over the range of numbers from 0 to 6 (inclusive) and assigns each value to
# the variable `_`. Then it prints the string "Hello, World" for each value in the range. This loop
# will execute seven times, printing "Hello, World" each time. The variable `_` is used as a
# placeholder for a value that is not actually used in the loop.
"""for _ in range(7):
    print("Hello, World")"""

# Printing the string "Hello, World" three times in a row.
"""print("Hello, World" * 3)"""

# Printing the string "Hello, World" three times in a row, with a newline character after each
# instance, and using the `end` parameter to prevent an additional newline character from being
# printed at the end.
"""print("Hello, World\n" * 3, end="")"""