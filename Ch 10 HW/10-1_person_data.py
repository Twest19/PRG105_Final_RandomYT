"""
    Design a class that holds the following personal data: name, address, age, and phone number.
    Write appropriate accessor and mutator methods (get and set). Write a program that creates three instances
    of the class. One instance should hold your information and the other two should hold your friends' or
    family members' information.  Just add information, don't get it from the user.  Print the data from each
    object, make sure to format the output for clarity and ease of reading.
"""


class Data:  # This class takes the data for a person and returns that data

    def __init__(self, name, address, age, phone='n/a'):
        self.name = name
        self.address = address
        self.age = age
        self.phone = phone

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_address(self, address):
        self.address = address

    def get_address(self):
        return self.address

    def set_age(self, age):
        self.age = int(age)

    def get_age(self):
        return self.age

    def set_phone(self, phone):
        self.phone = phone

    def get_phone(self):
        return self.phone

    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nAge: {self.age}\nPhone: {self.phone}\n"


def main():
    my_data = Data('Tim', '119 W South Ave', 21, '815-354-7216')
    friend_data = Data('Saul', '9800 Montgomery Blvd', 49, '505-503-4455')
    family_data = Data('Tom', '191 E North Ave', 42)
    print(my_data)
    print(friend_data)
    print(family_data)


main()
