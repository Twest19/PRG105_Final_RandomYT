"""
    Write a program that gathers contact information from people. The program should ask the user how many entries they
    are going to make, then ask for the Name, phone number, and email address for each person.

    You will be writing this information to a file. Separate each value with a comma, and make sure to
    include the new line symbol

    Write this program using a function  - you should just need the main function.
"""


def main():
    entries = int(input("How many people would you like to add to the file? "))
    for entries in range(0, entries):
        name = input("What is the person's name? ")
        phone_num = input("what is their phone number? ")
        email = input("What is their email address? ")
        file = open('contact_info.txt', 'a')
        file.write(f"{name}, {phone_num}, {email}\n")
        file.close()


main()
