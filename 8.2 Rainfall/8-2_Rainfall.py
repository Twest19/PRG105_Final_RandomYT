"""
    Download your start file for rainfall:
    Import the data from the file. Check to see if the data is valid, if it is not valid, indicate to the
    user what the bad data is. Total and average the data, and display formatted results on the screen.
"""


def main():
    file_name = open('rainfall-totals.txt', 'r')
    lines = file_name.readlines()
    rain = []
    for line in lines:
        x = line.split()
        rain.append(x)
    file_name.close()
    total = 0
    num_months = 0
    for j in range(len(rain)):
        try:
            y = float(rain[j][1])
        except ValueError:
            print(f"Sorry the data from {rain[j][0]} was invalid.")
        else:
            total += y
            num_months += 1
    avg = total / num_months
    print(f"\nThe total rainfall number for the year without the invalid data was {total:.2f}.")
    print(f"The average rainfall number per month was about {avg:.2f}.")


main()
