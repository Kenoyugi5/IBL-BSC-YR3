name = input("What's your name? ")

"""
# This code is opening a file named "names.txt" in append mode ("a"), which means that any new data
# written to the file will be added to the end of the existing data. It then writes the value of the
# `name` variable followed by a newline character to the file using the `write()` method. Finally, it
# closes the file using the `close()` method. This code is essentially adding the value of `name` to a
# list of names stored in the "names.txt" file.
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()
"""
# This code is opening a file named "name.txt" in append mode ("a") using a `with` statement, which
# ensures that the file is properly closed after the block of code is executed. It then writes the
# value of the `name` variable followed by a newline character to the file using the `write()` method.
# This code is essentially adding the value of `name` to a list of names stored in the "name.txt"
# file.
with open("name.txt", "a") as file:
    file.write(f"{name}\n")