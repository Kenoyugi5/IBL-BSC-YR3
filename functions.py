#This is the print function
"""This is the print function"""
print("Hello, World!")
print(2)
print(3.4)


#variables
x = 2
y = 3
print(x)
print(y)
print(x + y)
print(x * y)
name = input("What is your name?")
print(name)

first_number = int(input("What is your first"))
second_number = int(input("What is your second"))
print(first_number * second_number)


number_one = int(input("What is your first"))
number_two = int(input("What is your second"))
final_number = number_one + number_two
print(f"{final_number}")
print("{} + {} = {}".format(number_one, number_two, final_number))


a = float(input("Input first number")) # number 1
b = float(input("Input second number"))
c = a * b #C is a container to store the value of a*b
print(c)