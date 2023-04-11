import sys

def format_names(names):
    """
    The function formats a list of names into a farewell message.
    
    :param names: a list of strings representing names of people to say goodbye to
    :return: The function `format_names` takes a list of names as input and returns a farewell message
    that includes all the names in the list.
    """
    n = len(names)
    if n == 1:
        return f"Adieu, adieu, to {names[0]}"
    elif n == 2:
        return f"Adieu, adieu, to {names[0]} and {names[1]}"
    else:
        middle = ", ".join(names[1:-1])
        return f"Adieu, adieu, to {names[0]}, {middle}, and {names[-1]}"

# This code reads input from the command line and creates a list of names. It then calls the
# `format_names` function on each sublist of names, where each sublist contains the first i names from
# the original list. The function formats the names into a farewell message and returns it. Finally,
# the code prints out all the farewell messages, each on a new line.
names = []
for line in sys.stdin:
    name = line.strip()
    if name:
        names.append(name)

# This line of code is creating a farewell message for each sublist of names, where each sublist
# contains the first i names from the original list. It does this by using a generator expression to
# create a sequence of sublists, and then calling the `format_names` function on each sublist. The
# resulting farewell messages are then joined together with newline characters (`\n`) and printed out,
# each on a new line.
print("\n".join(format_names(names) for names in (names[:i] for i in range(1, len(names) + 1))))