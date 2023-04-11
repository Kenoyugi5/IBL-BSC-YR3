from collections import defaultdict

# Create a dictionary to store the number of times each item appears in the list
# `grocery_dict = defaultdict(int)` is creating a dictionary with default values of 0. This means that
# if a key is not found in the dictionary, it will automatically be assigned a value of 0.
grocery_dict = defaultdict(int)

# This code is creating an infinite loop that prompts the user to enter an item and then adds it to a
# dictionary called `grocery_dict`. The `item.lower()` method is used to convert the input to
# lowercase before adding it to the dictionary. If the user enters the end-of-file (EOF) character
# (usually Ctrl+D on Unix-based systems or Ctrl+Z on Windows), the loop is terminated with the
# `EOFError` exception and the program continues to the next section.
try:
    while True:
        item = input("Enter an item: ")
        grocery_dict[item.lower()] += 1
except EOFError:
    pass

# `items = sorted(grocery_dict.keys())` is creating a sorted list of all the keys in the
# `grocery_dict` dictionary. The `keys()` method returns a list of all the keys in the dictionary, and
# the `sorted()` function sorts the list in ascending order. The resulting list is assigned to the
# variable `items`.
items = sorted(grocery_dict.keys())

""" 
This code is iterating over the sorted list of keys in the `grocery_dict` dictionary and printing the count
of each item in the list. For each item in the list, it retrieves the count of that item from
the `grocery_dict` dictionary and prints it along with the item name in uppercase letters.
The `f"{count} {item.upper()}"` syntax is using f-strings to format the output string with the count
and item name. The `item.upper()` method is used to convert the item name to uppercase letters before printing.
for item in items:
"""
count = grocery_dict[item]
print(f"{count} {item.upper()}")
