with open("name.txt", "r") as file:
    for line in file:
        print("Hello,", line.rstrip())

"""
with open("name.txt", "r") as file:
    lines = file.readlines()


# This code is reading the contents of a file named "name.txt" and storing each line of the file as an
# element in a list called `lines`. Then, it is iterating through each element in the `lines` list and
# printing it to the console. Essentially, it is printing the contents of the "name.txt" file to the
# console.
"""
"""
for line in lines:
    print(line)
"""
"""
# This code is iterating through each element in the `lines` list and printing a greeting message
# "Hello," followed by the content of each line in the list with any trailing white space removed
# using the `rstrip()` method. Essentially, it is printing a personalized greeting message to each
# name listed in the "name.txt" file.
"""
"""for line in lines:
    print("Hello,",line.rstrip())
"""
"""
"""