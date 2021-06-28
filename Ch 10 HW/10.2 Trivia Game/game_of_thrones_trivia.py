"""


"""

from question_class import Question


def main():
    questions = [
        Question("What is the name of Jon Snow's direwolf?", "(A) Ghost", "(B) Nymeria", "(C) Summer",
                 "(D) Lady\n", "A"),
        Question("What house does Reek belong too?", "(A) Bolton", "(B) Stark", "(C) Greyjoy",
                 "(D) Lannister\n", "C"),
        Question("Which house has a dragon as it's sigil?", "(A) Stark", "(B) Baratheon", "(C) Martell",
                 "(D) Targaryen\n", "D"),
        Question("Who is the Onion Knight?", "(A) Ser Davos Seaworth", "(B) Ser Jamie Lannister",
                 "(C) Brienne of Tarth", "(D) Ser Jorah Mormont\n", "A"),
        Question("Who is The Hound's brother?", "(A) Robert Baratheon", "(B) The Mountain", "(C) Tyrion",
                 "(D) Hodor\n", "B"),
    ]

    players = {'player one': 0, 'player two': 0}  # Dictionary of the players and their scores

    print(f"{'='*5} Game of Thrones Mini Quiz {'='*5}")
    for player in players:
        print(f"{'='*6} {player.title()} begin {'='*6}")
        for q in questions:
            print(q.get_question())
            print(q.get_ans1())
            print(q.get_ans2())
            print(q.get_ans3())
            print(q.get_ans4())
            guess = input("Enter the letter of your answer: ")
            if guess.upper() == q.get_answer():
                print("Correct\n")
                players[player] += 1
            else:
                print("Incorrect\n")
        print(f"{player.title()} got a total of {players[player]} point(s).\n")

    if players['player one'] > players['player two']:
        print(f"\n{'='*5} Congratulations Player One! You are the winner! {'='*5}")
    elif players['player two'] > players['player one']:
        print(f"\n{'='*5} Congratulations Player Two! You are the winner! {'='*5}")
    else:
        print(f"\n{'='*5} Looks like there is a tie! You are both winners! {'='*5}")


main()

while True:  # Gives the option to play again
    prompt = input("\nWould you like to play again (Yes or No)? ").lower()
    if prompt == 'yes':
        main()
    else:
        break
