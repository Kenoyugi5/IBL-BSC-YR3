def main():
    x = int(input("What is the value of x? "))
    if mod(x):
        print("Even")
    else:
        print("Odd")


def mod(n):
    # `return n % 2 == 0` is a boolean expression that checks if the remainder of `n` divided by 2 is
    # equal to 0. If it is, then the function returns `True`, indicating that `n` is an even number.
    # If it's not, then the function returns `False`, indicating that `n` is an odd number.
    return n % 2 == 0
    
main()