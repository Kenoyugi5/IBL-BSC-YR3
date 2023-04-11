def main():
    """
    The function takes a user input in camel case and converts it to snake case.
    """
    camel_name = input("Enter a name in camel case: ")
    snake_name = convert_to_snake(camel_name)
    print("The snake case version is:", snake_name)


def convert_to_snake(camel_name):
    snake_name = ""
   # This code is iterating over each character in the input string `camel_name` using the
   # `enumerate()` function. For each character, it checks if it is uppercase using the `isupper()`
   # method. If it is uppercase, it adds an underscore to the `snake_name` string (except for the
   # first character) and then adds the lowercase version of the character to the `snake_name` string.
   # If the character is not uppercase, it simply adds it to the `snake_name` string as is. This
   # process continues until all characters in the input string have been processed, and the final
   # `snake_name` string is returned.
    for i, char in enumerate(camel_name):
        if char.isupper():
            if i != 0:
                snake_name += "_"
            snake_name += char.lower()
        else:
            snake_name += char
    return snake_name


if __name__ == "__main__":
    main()
