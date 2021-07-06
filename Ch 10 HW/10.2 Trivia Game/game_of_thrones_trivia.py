"""
    In this programming exercise, you will create a simple trivia game for two players. 
    The program will work like this: 

    Starting with player 1, each player gets a turn at answering 5 trivia questions. 
    (There should be a total of 10 questions.) When a question is displayed, 4 possible answers are also displayed. 
    Only one of the answers is correct, and if the player selects the correct answer, he or she earns a point. 
    After answers have been selected for all the questions, the program displays the number of points earned by each 
    player and declares the player with the highest number of points the winner.
    
    To create this program, write a Question class to hold the data for the trivia question. The question class 
    should have attributes for the following data:
    
    A trivia question
    Possible answer 1
    Possible answer 2
    Possible answer 3
    Possible answer 4
    The number of the correct answer (1, 2, 3, or 4)
    The Question class should also have an appropriate __init__ method, accessors, and mutators. 

    The program should have a list or a dictionary containing 10 Question Objects, one for each trivia question. 
    Make up your own trivia question on the subject or subjects of your choice for the objects.
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
        Question("What is Jon Snow's sword named?", "(A) Oathkeeper", "(B) Longclaw", "(C) The Wall",
                 "(D) Widow's Wail\n", "B"),
        Question("How many dragons did Daenarys Targaryen have?", "(A) 5", "(B) 2", "(C) 1",
                 "(D) 3\n", "D"),
        Question("What is Catelyn Stark's maiden name?", "(A) Baratheon", "(B) Martell", "(C) Tully",
                 "(D) Frey\n", "C"),
        Question("In what episode is the Red Wedding?", "(A) The Rains of Castamere", "(B) The Queens Justice",
                 "(C) Kissed by Fire", "(D) Mother's Mercy\n", "A"),
        Question("Who is The King Beyond the Wall?", "(A) Tormund Giantsbane", "(B) Jon Snow", "(C) Crastor",
                 "(D) Mance Rayder\n", "D"),
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
