def main():
    """
    The function prompts the user to input a greeting and then prints the value returned by the function
    "value" when passed the greeting as an argument.
    """
    greeting = input("Kindly enter your greeting: ")
    print("The value is:", value(greeting))

def value(greeting):
    """
    The function returns a value based on whether the input string starts with "hello", "h", or anything
    else.
    
    :param greeting: a string representing a greeting message
    :return: an integer value based on the input string `greeting`. If the input string starts with
    "hello" (case-insensitive), it returns 0. If it starts with "h" (case-insensitive), it returns 20.
    Otherwise, it returns 100.
    """
    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()