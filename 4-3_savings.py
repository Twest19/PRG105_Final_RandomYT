"""
    Write a program that projects yearly income, the amount saved towards retirement each year, and total retirement
    savings.  Assume a 3 percent raise on the starting income each year, and a 6% yearly return on investment. You will
    need to ask the user their current age, at what age they want to retire, what their current income is, what percent
    of their income they save each year, and how much they currently have in savings. ou will calculate how many years
    until retirement, and display the projected income, savings contribution, and total savings each year.
"""

# Ask user for the appropriate information
age = int(input("What is your current age? "))
retire = int(input("At what age do you want to retire? "))
income = int(input("What is your current yearly income? "))
save_year = int(input("What percent of your income do you save every year? "))
current_savings = int(input("How much do you currently have in your savings? "))

# Notify them of how these numbers are calculated
print("\n*This assumes a yearly raise of 3% and a yearly return on investment of 6%")

# Some calculations to figure out the correct data for the table
years = retire - age
save_year = save_year / 100
contribution = income * save_year

# make sure you multiple savings by 6% before adding the contribution
total_save = current_savings * 1.06 + contribution

# Format a heading for each category
print(f"\n{'Year'}{'Income':>12}{'Savings Contribution':>26}{'Total Savings':>19}")

# Create a for loop to cycle through correct amount of years until retirement and place data accordingly
for year in range(1, years + 1):
    print(f"{year:>4}{income:>12,.0f}{contribution:>26,.0f}{total_save:>19,.0f}")
    income = income * 1.03
    contribution = income * save_year
    total_save *= 1.06
    total_save += contribution
