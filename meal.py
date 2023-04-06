def main():
    time = input("What is the time? ")
    if 7.0 <= convert(time) <= 8.00:
        print("Breakfast time")
    elif convert(time) >= 12.0 and convert(time) <= 13.00:
        print("Lunch time")
    elif convert(time) >= 18.0 and convert(time) <= 19.00:
        print("Dinner time")
    else:
        print("Sorry, it is not yet meal time")

def convert(time):
    hour, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes/100
    return hours + minutes

main()