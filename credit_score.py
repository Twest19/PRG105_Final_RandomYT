"""
Ask your user for their credit score. Tell them if they have Bad, Fair, Good, or Excellent credit.
"""

user_score = int(input("What is your credit score? "))

if user_score >= 720:
	print(f"A credit score of {user_score} is an excellent credit score.")
elif 690 <= user_score < 720:
	print(f"A credit score of {user_score} is a good credit score.")
elif 630 <= user_score < 690:
	print(f"A credit score of {user_score} is a fair credit score.")
else:
	print(f"A credit score of {user_score} is a bad credit score.")
