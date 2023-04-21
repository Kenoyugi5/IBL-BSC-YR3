import sys
from datetime import date, datetime

def get_date_of_birth():
    """
    Prompt the user for their date of birth in YYYY-MM-DD format.
    """
    date_str = input("Please enter your date of birth in YYYY-MM-DD format: ")
    try:
        date_of_birth = datetime.strptime(date_str, "%Y-%m-%d").date()
        return date_of_birth
    except ValueError:
        print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
        sys.exit()

def age_in_minutes(date_of_birth):
    """
    Calculate the age of the user in minutes.
    """
    now = date.today()
    age_in_seconds = (now - date_of_birth).total_seconds()
    age_in_minutes = age_in_seconds // 60
    return int(age_in_minutes)

def convert_to_words(num):
    """
    Convert a number to English words.
    """
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    
    if num == 0:
        return "zero"
    
    if num < 10:
        return ones[num]
    
    if num < 20:
        return teens[num-10]
    
    if num < 100:
        return tens[num//10] + (" " + ones[num%10] if ones[num%10] != "" else "")
    
    if num < 1000:
        return ones[num//100] + " hundred" + (" and " + convert_to_words(num%100) if num%100 != 0 else "")
    
    if num < 1000000:
        return convert_to_words(num//1000) + " thousand" + (" " + convert_to_words(num%1000) if num%1000 != 0 else "")
    
    if num < 1000000000:
        return convert_to_words(num//1000000) + " million" + (" " + convert_to_words(num%1000000) if num%1000000 != 0 else "")
    
    return ""

def main():
    date_of_birth = get_date_of_birth()
    age = age_in_minutes(date_of_birth)
    age_words = convert_to_words(age)
    print(f"You are {age_words} minutes old.")

if __name__ == "__main__":
    main()