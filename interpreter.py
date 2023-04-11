def main():
    """
    This Python function takes a mathematical expression as input and evaluates it, returning the result
    rounded to one decimal place.
    """
    expression = input("Enter expression: ")
    x, y, z = expression.split()
    x = int(x)
    z = int(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        print("Invalid expression")
    
    print(f"{result:.1f}")

if __name__ == "__main__":

    main()