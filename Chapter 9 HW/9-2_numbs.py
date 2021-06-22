"""
    Create a quiz based on learning the numbers from 1-10 in another language.

    Create a dictionary based on the language of your choice with the numbers from 1-10 paired with the
    numbers from 1-10 in English. Create a quiz based on this dictionary. Display the number in a foreign language
    and ask for the number in English. Score the test and give the user a letter grade.
"""


def main():
    num_dict = {'one': 'eins', 'two': 'zwei', 'three': 'drei', 'four': 'vier',
                'five': 'funf', 'six': 'sechs', 'seven': 'sieben', 'eight': 'acht',
                'nine': 'neun', 'ten': 'zehn'}
    print("Enter the number in English that is the same as the number in German.\n")
    correct = 0

    for k, v in num_dict.items():
        answer = input(f"What is the equivalent of {v} in English? ").lower()
        if answer == k:
            print(f"{k.title()} is correct!\n")
            correct += 1
        else:
            print(f"Sorry, {answer} is incorrect.\n")

    print(f"\nYou got a total of {correct} out of {len(num_dict)} answers correct.")
    grade = (correct / len(num_dict)) * 100
    if grade >= 90:
        letter_grade = 'A'
    elif grade >= 80:
        letter_grade = 'B'
    elif grade >= 70:
        letter_grade = 'C'
    elif grade >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'
    print(f"Which is a letter grade of {letter_grade}.")


main()
