import random


def main():
    """
    This function generates 10 addition problems of varying difficulty based on the user's chosen level
    and prompts the user to input the correct answer, giving feedback and keeping score.
    """
    level = get_level()
    score = 0
    for i in range(10):
        x, y = generate_integer(level)
        problem = f"{x} + {y} = "
        for j in range(3):
            answer = input(problem)
            try:
                answer = int(answer)
                if answer == x + y:
                    print("Correct!")
                    score += 1
                    break
                else:
                    if j < 2:
                        print("EEE")
                    else:
                        print(f"The correct answer is {x + y}")
            except ValueError:
                if j < 2:
                    print("EEE")
                else:
                    print(f"The correct answer is {x + y}")
    print(f"Your score is {score} out of 10.")


def get_level():
    """
    This function prompts the user to enter a level (1, 2, or 3) and returns the inputted level after
    validating it.
    :return: the user inputted level as an integer (either 1, 2, or 3).
    """
    level = None
    while level not in [1, 2, 3]:
        try:
            level = int(input("Enter level (1, 2, or 3): "))
            if level not in [1, 2, 3]:
                print("Invalid input. Please try again.")
        except ValueError:
            print("Invalid input. Please try again.")
    return level


def generate_integer(level):
    """
    This function generates two random integers with a number of digits based on the input level.
    
    :param level: The level parameter is an integer that determines the number of digits in the randomly
    generated integers. If level is 1, the integers will have 1 digit, if level is 2, the integers will
    have 2 digits, and if level is 3, the integers will have 3 digits
    :return: a tuple of two randomly generated integers, x and y, where the number of digits in each
    integer is determined by the input level.
    """
    if level == 1:
        num_digits = 1
    elif level == 2:
        num_digits = 2
    else:
        num_digits = 3
    x = random.randint(0, 10**num_digits - 1)
    y = random.randint(0, 10**num_digits - 1)
    return x, y


main()
