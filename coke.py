print("Coke Price: 50") #Informing the user on the price of Coke
total = 50
amount_added = 0

# This code block is creating a loop that will continue to ask the user to insert a coin until the
# total amount paid is equal to or greater than 50 cents. The user can only insert coins of 5, 10, or
# 25 cents. The code subtracts the value of the coin inserted from the total price of the coke and
# adds the value of the coin to the amount added variable. If the total amount added is equal to or
# greater than 50 cents, the code will print the change and end the loop. If the total amount added is
# less than 50 cents, the code will print the amount due and continue the loop.
while True:
    paid = int(input("Insert a coin (5, 10, or 25 cents): "))
    if paid == 25 or paid == 10 or paid == 5:
        total = total - paid
        amount_added += paid

    else:
        print( "amount due: " ,total)

    if amount_added>=50:#conditional statement if coins added are more than 50 to end the code
        print("Change= ", amount_added-50)
        break

    else:#if not the code continues
        print( "amount due: ",total)