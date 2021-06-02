"""
    Write a program that asks a user to enter a whole number between 20 and 100. Send that number to a function that
    will validate the number, and if it is not a number between 20 and 100, use a while loop to keep asking the user
    for a valid number. Return the number to the main function (hint good_number = validate(num) - use a variable to
    store the returned value).

    You will also program three functions that determine if the number is divisible by two, by three, and by five.

    You will have a final function that puts output on the screen - identifying if the number is divisible by two,
    three, and five.
"""


def main():
    while True:
        prompt1 = int(input("Enter a whole number between 20 and 100: "))
        if prompt1 in range(20, 101):
            good = validate(prompt1)
            print(f"Your number is {good}")
            divisible_2(good)
            divisible_3(good)
            divisible_5(good)
            identify(good)
            break
        else:
            print("Error, please try again.")
            continue


def validate(x):
    num = x
    return num


def divisible_2(x):
    if x % 2 == 0:
        return True
    else:
        return False


def divisible_3(x):
    if x % 3 == 0:
        return True
    else:
        return False


def divisible_5(x):
    if x % 5 == 0:
        return True
    else:
        return False


def identify(x):
    if divisible_2(x) is True:
        print(f"{x} is divisible by two")
    else:
        print(f"{x} is not divisible by two")

    if divisible_3(x) is True:
        print(f"{x} is divisible by three")
    else:
        print(f"{x} is not divisible by three")

    if divisible_5(x) is True:
        print(f"{x} is divisible by five")
    else:
        print(f"{x} is not divisible by five")


main()
