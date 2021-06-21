"""
    Create dictionaries
    Use for loops with dictionaries

    You will be tracking the number of steps someone takes each day for a week. Using a loop, ask them to enter
    the date and the number of steps. At the end of the program, you will display the total number of steps taken,
    the day with the most steps, and the day with the least steps. Print multiple days if they are tied.
"""


def main():
    print("For each day of the week enter the number of steps taken for that day.")
    days_steps = {}
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    for day in days:
        prompt = int(input(f"Enter the number of steps taken on {day}: "))
        days_steps[day] = prompt

    total = 0
    max_key = []
    min_key = []
    for key, values in days_steps.items():
        total += values
        if values == max(days_steps.values()):
            max_key.append(key)
        elif values == min(days_steps.values()):
            min_key.append(key)

    print(f"\nYou walked a total of {total:,} steps this week.")
    print(f"You averaged {int(total/len(days_steps)):,} steps per day.")
    print(f"The most amount of steps you took was {max(days_steps.values()):,} on {', '.join(max_key)}.")
    print(f"The least amount of steps you took was {min(days_steps.values()):,} on {', '.join(min_key)}.")


main()
