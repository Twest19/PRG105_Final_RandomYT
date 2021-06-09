"""
    Open the file sales_totals download in read mode
    Read in all the lines using a loop
    Strip the newline symbol and convert each line to a float
    Add each number to the running total
    Count the number of lines
    Format and display each number
    Outside of the loop format and display the total, the count, and the average
    Do this in functions
"""
# create a main function to do the reading of the lines and printing of the total, average, entries


def main():
    sales_file = open('sales_totals-1.txt', 'r')
    count = 0
    total = 0
    line = sales_file.readline()
    while line != '':
        print(f"{float(line):,.2f}")
        total += float(line)
        line = sales_file.readline()
        count += 1
    sales_file.close()
    avg = average(total, count)
    print(f"Total: {total:,.2f}")
    print(f"Number of entries: {count}")
    print(f"Average: {avg:,.2f}")


# created an average function to find the average


def average(x, y):
    avg = x / y
    return avg


main()
