# `import random` is importing the `random` module in Python, which provides functions for generating
# random numbers and other random operations.
import random

# This code block is prompting the user to enter a level and then checking if the input is a valid
# integer greater than 0. If the input is valid, the loop is broken and the program moves on to the
# next block of code. If the input is not valid, the loop continues and the user is prompted to enter
# a valid input again.
while True:
    random_level = input("Enter a level: ")
    try:
        level = int(random_level)
        if level > 0:
            break
    except ValueError:
        pass
    print("Invalid input, please try again.")

# `number = random.randint(1, level)` is generating a random integer between 1 and the value of
# `level` (inclusive) and assigning it to the variable `number`.
number = random.randint(1, level)

while True:
    guess_str = input("Guess a number between 1 and {}: ".format(level))
    try:
        guess = int(guess_str)
        if guess <= 0:
            raise ValueError
    except ValueError:
        print("Invalid input, please try again.")
        continue

    if guess < number:
        print("Too small!")
    elif guess > number:
        print("Too large!")
    else:
        print("Just right!")
        break
