# This code takes user input for a text and removes all the vowels (both uppercase and lowercase) from
# the text using the `replace()` method. The vowels are defined in a tuple called `vowels`. The
# modified text is then printed as output.
vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
word = input("Enter some text: ")
for vowel in vowels:
    word = word.replace(vowel, "")
print("New text: ", word)