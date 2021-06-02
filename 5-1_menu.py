"""
    Create a program that presents the user with five choices. The topic could be game characters, food, car packages,
    anything you are interested in. You will put a menu on the screen, ask the user to enter the number or letter of
    their choice, and then call the corresponding function to give the user more information.
"""
# Create a main function that will hold the user input statement and menu options


def main():
    print("Choose one of the menu options below for more details")
    print("(A) Single Cheeseburger\n"
          "(B) Double Cheeseburger\n"
          "(C) Chicago Style Hot dog\n"
          "(D) Basket of Fries\n"
          "(E) Ice Cream Sundae\n")
    while True:
        prompt1 = input("Please enter the letter next to the item of your choice or type 'q' to quit: ").upper()
        if prompt1 in ('A', 'B', 'C', 'D', 'E'):
            if prompt1 == 'A':
                single_cheese()
                break
            elif prompt1 == 'B':
                double_cheese()
                break
            elif prompt1 == 'C':
                cs_dog()
                break
            elif prompt1 == 'D':
                basket_fry()
                break
            elif prompt1 == 'E':
                sundae()
                break
        elif prompt1 == 'Q':
            print("Goodbye!")
            break
        else:
            print("Error, please try again.\n")
            continue
# create functions for each menu option to be called upon


def single_cheese():
    print("\nSingle Cheeseburger")
    print("With your choice of toppings.")
    print("Served with a side of fries or onion rings.")


def double_cheese():
    print("\nDouble Cheeseburger")
    print("With your choice of toppings.")
    print("Served with a side of fries or onion rings.")


def cs_dog():
    print("\n1 Chicago Style Hot Dog")
    print("With your choice of toppings.")
    print("Served with a side of fries or onion rings.")


def basket_fry():
    print("\nA Basket of Fries")
    print("With your choice of condiments or the option to make them cheese or chili fries.")


def sundae():
    print("\nIce Cream Sundae")
    print("Available in chocolate, vanilla, or strawberry.")
    print("With your choice of toppings.")


main()
