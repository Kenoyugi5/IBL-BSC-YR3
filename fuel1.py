def main():
    """
    This function prompts the user to input a fuel fraction, calculates the percentage of fuel
    remaining, and outputs a corresponding letter grade or percentage.
    """
    while True:
        try:
            fuel = input("Enter fuel fraction (X/Y): ")
            x, y = fuel.split("/")
            x = int(x)
            y = int(y)
           # This code block is checking if the input values for `x` and `y` are valid. If `x` or `y`
           # is less than or equal to 0 or if `x` is greater than `y`, it raises a `ValueError`
           # exception. If the input is valid, it breaks out of the `while` loop. If there is an
           # exception raised, it catches the exception and prints an error message asking the user to
           # try again.
            if x <= 0 or y <= 0 or x > y:
                raise ValueError
            break
        except (ValueError, ZeroDivisionError):
            print("Please try again.")
    
    percentage = x / y * 100
    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(round(percentage))

main()