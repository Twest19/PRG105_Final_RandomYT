"""
    You need to create a program that will have the user enter in the total sales amount for the day at a coffee shop.
    The program should ask the user for the total amount of sales and include the day in the request. At the end of
    data entry, tell the user the total sales for the week, and the average sales per day. You must create a list of
    the days of the week for the user to step through, see the example output.
"""

days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
weekly_total = 0

print("Sales for the week:")
for day in days:
    sales = float(input(f"What was the total amount of sales on {day}? "))
    weekly_total += sales

print(f"\nThe total amount of sales for the week was: ${weekly_total:,.2f}")
print(F"The average amount of sales per day was: ${weekly_total / 7:,.2f}")
