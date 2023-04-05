def main():
    x = int(input("What is the value of x? "))
    # The code is checking if the value of `x` is even or odd. It does this by calling the `mod`
    # function with `x` as an argument. If the `mod` function returns `True`, indicating that `x` is
    # even, then the code prints "Even". Otherwise, if the `mod` function returns `False`, indicating
    # that `x` is odd, then the code prints "Odd".
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