"""
    Write a CRUD - Create, Read, Update, Delete application
    Pickle files and save them
    Unpickle and save into data structures

    Write a program that keeps names and email addresses in a dictionary as key-value pairs. The program should
    display a menu that lets the user look up a person's email address, add a new name and email address,
    change an existing email address, and delete an existing name and email address. The program should pickle
    the dictionary and save it to a file when the user exits the program. Each time the program starts,
    it should retrieve the dictionary from the file and unpickle it.
"""

import pickle

# Global values
LOOK_UP = 1
ADD_NEW = 2
CHANGE_OLD = 3
DELETE_OLD = 4
QUIT = 5


def main():
    try:
        file = open("customer_file.dat", 'rb')
        customer_info = pickle.load(file)
    except (FileNotFoundError, IOError):
        print("Sorry that file was not found, please add a customer then quit to make the file.")
        customer_info = {}

    choice = 0

    while choice != 5:
        choice = menu()
        if choice == 1:
            look_up(customer_info)
        elif choice == 2:
            add_new(customer_info)
        elif choice == 3:
            change(customer_info)
        elif choice == 4:
            delete(customer_info)
        elif choice == 5:
            save_info(customer_info)


def menu():
    print(f"\n{'='*24}")
    print("Email Address/ Name Info")
    print(f"{'='*24}")
    print("Please choose one of the following options:")
    print("(1) Look up a name")
    print("(2) Add a new email/name")
    print("(3) Change an existing email/name")
    print("(4) Delete an existing email/name")
    print("(5) Exit\n")

    choice = int(input("Please enter the number for the option you want: "))
    while choice not in range(1, 6):
        choice = int(input("\nError, please try again: "))
    return choice


def look_up(customer):
    print(f"\n{'='*42}")
    print(f"{'='*12} Customer Look Up {'='*12}")
    look_person = input("Please input a person's name: ").title()
    if look_person in customer:
        print(f"\n{look_person}'s email is {customer.get(look_person)}.")
    else:
        print("\nSorry, that person's name cannot be found.")


def add_new(customer):
    print(f"\n{'='*38}")
    print(f"{'='*12} Add Customer {'='*12}")
    name = input("Please enter a name: ").title()
    email = input("Please enter a email: ")
    if name in customer:
        print("\nSorry, that person already has an account.")
    else:
        customer[name] = email
        print(f"\n{name} and the email {customer[name]} have been added.")


def change(customer):
    print(f"\n{'='*41}")
    print(f"{'='*12} Change Customer {'='*12}")
    name = input("Please enter the person's name for the email you want to change: ").title()
    if name in customer:
        change_email = input("Now enter the new email: ")
        customer[name] = change_email
        print(f"\n{name}'s email has been changed to {customer[name]}.")
    else:
        print("\nSorry, that person's name cannot be found.")


def delete(customer):
    print(f"\n{'='*41}")
    print(f"{'='*12} Delete Customer {'='*12}")
    delete_name = input("Enter the name associated with the account you wish to delete: ").title()
    if delete_name in customer:
        print(f"\nThe account associated with the name {delete_name} and email {customer[delete_name]} "
              f"have been deleted.")
        del customer[delete_name]
    else:
        print("\nSorry, that person's name cannot be found.")


def save_info(customer):
    print(f"\n{'='*24}")
    print(f"\nSaving your changes...")
    save_file = open("customer_file.dat", 'wb')
    pickle.dump(customer, save_file)
    save_file.close()
    print("\nYour changes have been saved!\n")
    print('Goodbye!')
    print(f"{'='*24}")


main()
