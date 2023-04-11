def main():
    """
    The function calculates the tip amount for a meal based on the meal cost and the desired tip
    percentage.
    """

    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")
    
def dollars_to_float(d):
    d = d.replace("$", "")
    d = float(d)
    return round(d)

def percent_to_float(p):
    p = p.replace("%", "")
    p = float(p) / 100
    return p


main()