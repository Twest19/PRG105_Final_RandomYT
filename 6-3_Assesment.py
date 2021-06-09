"""
    Use the program from 6.2 as a start
    Open the sales_error.txt file as the infile
    One of the numbers has an error - use the try and except statement to make it ignore the line with the error,
    report it to the screen.
    Also detect if there is a bad file name, test that by looking for a bad filename
"""


def main():
    filename = 'sales_error.txt'
    try:
        with open(filename, 'r') as sales_file:
            count = 0
            line = sales_file.readline()
            while line != '':
                try:
                    count += 1
                    print(f"{float(line):,.2f}")
                    line = sales_file.readline()
                except ValueError:
                    print(f"Line {count} with a value of {line.rstrip()} was invalid.")
                    break
            sales_file.close()
    except IOError:
        print(f"{filename} does not exist.")


main()
