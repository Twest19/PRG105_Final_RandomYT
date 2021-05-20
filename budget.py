"""
Create a program that helps someone create a budget. It should ask the user for monthly income and the following expenses
Housing
Food
Transportation
Phone
Utilities
Clothing
"""

# Ask the user for their monthly expenses
monthly_income = int(input("What is your total net monthly income? "))
exp_housing = int(input("How much do you spend each month on housing? "))
exp_food = int(input("How much do you spend each month on food? "))
exp_transportation = int(input("How much do you spend each month on transportation? "))
exp_phone = int(input("How much do you spend each month on a phone bill? "))
exp_utilities = int(input("How much do you spend each month on utilities? "))
exp_clothing = int(input("How much do you spend each month on clothing? "))

# Find the decimal value by dividing the expense by monthly income
percent_housing = exp_housing / monthly_income
percent_food = exp_food / monthly_income
percent_transportation = exp_transportation / monthly_income
percent_phone = exp_phone / monthly_income
percent_utilities = exp_utilities / monthly_income
percent_clothing = exp_clothing / monthly_income

# Convert the decimal to a percent and display
print(f"\nHousing takes up {percent_housing:.2%} of your monthly budget")
print(f"Food takes up {percent_food:.2%} of your monthly budget")
print(f"Transportation takes up {percent_transportation:.2%} of your monthly budget")
print(f"Phone bill takes up {percent_phone:.2%} of your monthly budget")
print(f"Utilities takes up {percent_utilities:.2%} of your monthly budget")
print(f"Clothing takes up {percent_clothing:.2%} of your monthly budget")

# Calculate total expenses and how much income is left after expenses and display
total_expenses = exp_housing + exp_food + exp_transportation + exp_phone + exp_utilities + exp_clothing
income_left = monthly_income - total_expenses

print(f"\nYour total expenses for the month are: ${total_expenses:,.2f}")
print(f"\nYour total income after expenses is: ${income_left:,.2f}")
