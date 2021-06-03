"""
    You are going to write a program that finds the area of a shape for the user.
"""
# set PI as a constant to be used as a global value
PI = 3.14

# create a main function then from the main function call other functions to get the correct calculations


def main():
    while True:
        menu()
        choice = int(input("Enter the number of your selection: "))
        num = validate(choice)
        if num == 1:
            base = int(input("Enter the base of the rectangle in cm: "))
            height = int(input("Enter the height of the rectangle in cm: "))
            area = rectangle(base, height)
            print(f"The area of the rectangle is {area:.2f} square cm.")
        elif num == 2:
            base = int(input("Enter the base of the triangle in cm: "))
            height = int(input("Enter the height of the triangle in cm: "))
            area = triangle(base, height)
            print(f"The area of the triangle is {area:.2f} square cm.")
        elif num == 3:
            side = int(input("Enter the length of one side of the square in cm: "))
            area = square(side)
            print(f"The area of the square is {area:.2f} square cm.")
        elif num == 4:
            radius = int(input("Enter the radius of the circle: "))
            area = circle(radius)
            print(f"The area of the circle is {area:.2f} square cm.")

# menu function displays the options available to the user


def menu():
    print("\nThis program will find the area of any of the shapes below.")
    print("1. Rectangle\n"
          "2. Triangle\n"
          "3. Square\n"
          "4. Circle\n"
          "5. Quit\n")

# The validate function confirms the users input if the users provides a correct response


def validate(x):
    while True:
        if 1 <= x < 5:
            return x
        elif x == 5:
            print("\nGoodbye!")
            exit()
        else:
            print("\nError, please try again.\n")
            x = int(input("Enter the number of your selection: "))
            continue

# Create a function for each of the shapes to calculate the area for the corresponding shape


def rectangle(x, y):
    area = x * y
    return area


def triangle(x, y):
    area = x * y * 1/2
    return area


def square(x):
    area = x**2
    return area


def circle(r):
    global PI
    area = PI * r**2
    return area


main()
