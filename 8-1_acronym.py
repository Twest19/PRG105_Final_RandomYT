"""
    Slice strings
    Select specific letters from strings
    Use string modification methods

    Get a phrase from the user
    Split the phrase into a list
    Use the first letter of each word to create the acronym
    Change the acronym to all caps
    Display the acronym on screen
"""


def main(phrase):
    words = phrase.split()
    acronym = ''
    for letter in words:
        x = letter[0]
        acronym += x
    return acronym.upper()


print(main(input("Enter a phrase to get the acronym: ").lower()))
