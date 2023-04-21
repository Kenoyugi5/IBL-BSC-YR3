def main():
    """
    This Python function prompts the user for an IPv4 address and validates whether it is valid or not.
    """
    ip = input("IPv4 Address: ")
    if validate(ip):
        print("Valid IPv4 address")
    else:
        print("Invalid IPv4 address")

def validate(ip):
    """
    The function validates if a given IP address is in the correct format and within the valid range.
    
    :param ip: The input parameter "ip" is a string representing an IP address in the format
    "xxx.xxx.xxx.xxx", where each "xxx" is a number between 0 and 255 inclusive. The function "validate"
    checks whether the input string is a valid IP address or not, and returns True if
    :return: a boolean value (True or False) depending on whether the input string `ip` is a valid IPv4
    address or not.
    """
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if int(part) < 0 or int(part) > 255:
            return False
    return True


if __name__ == "__main__":
    main()
