import re
import sys

def main():
    print(count(input("Text: ")))

def count(s):
    # Use regex to find all occurrences of "um" as a word unto itself, case-insensitively
    pattern = r'\bum\b'
    matches = re.findall(pattern, s, re.IGNORECASE)
    return len(matches)

if __name__ == "__main__":
    main()