"""
# `import validators` is importing the `validators` library in Python, which provides functions to
# validate various types of data such as email addresses, URLs, IP addresses, etc.
import validators

def main():
    
    #This Python function prompts the user to enter an email address and checks if it is valid using the
    #validators library.
        
    email = input("Enter your email address: ")
    if validators.email(email):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
"""