menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# This is a Python code that prompts the user to enter items from a menu and calculates the total cost
# of the items entered.
total = 0.0
while True:
    try:
        item = input("Enter an item: ").strip().title()
        if item not in menu:
            continue
        total += menu[item]
        print(f"Total cost: ${total:.2f}")
   # `except EOFError: break` is a try-except block that catches the `EOFError` exception and breaks
   # out of the while loop. `EOFError` is raised when the user enters the end-of-file (EOF) character,
   # which is typically Ctrl+D on Unix-based systems or Ctrl+Z on Windows. This allows the user to
   # exit the program gracefully without causing an error.
    except EOFError:
        break
    """Enter control -z to exit"""
