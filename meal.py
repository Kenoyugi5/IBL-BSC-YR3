def main():
    """
    The function takes user input for time in 24-hour format, converts it to decimal format, and prints
    a message based on whether it's breakfast, lunch, or dinner time.
    """
    time_str = input("What's the time(24hr format)? ")
    time = convert(time_str)
    if 7 <= time < 8:
        print("It's breakfast time!")
    elif 12 <= time < 13:
        print("It's lunch time!")
    elif 18 <= time < 19:
        print("It's dinner time!")


def convert(time):
    hours, minutes = time.split(":")
    return float(hours) + float(minutes) / 60


if __name__ == "__main__":
    main()