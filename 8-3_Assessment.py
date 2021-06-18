"""
    Match strings in a list
    Error Checking
    Download both files: accounts.txt over90.txt
    Read both files into lists. Print the complete customer information on the screen if they are on both lists.
    Do error checking for file names to make sure the files exist (try and except statements.)
"""


def main():
    stop = False
    accounts = []
    file_a = 'accounts.txt'
    try:
        file_one = open(file_a, 'r')
    except IOError:
        print("Sorry the file", file_a, "does not exist.")
        stop = True
    else:
        lines = file_one.readlines()
        for line in lines:
            x = line.split()
            accounts.append(x)
        file_one.close()

    over = []
    file_b = 'over90.txt'
    try:
        file_two = open(file_b, 'r')
    except IOError:
        print("Sorry the file", file_b, "does not exist")
        stop = True
    else:
        num = file_two.readlines()
        for n in num:
            y = n.split()
            over.append(y)
        file_two.close()
        
    if stop is False:  # This code will only run if the correct file is found
        print(f"The following accounts are at least 90 days over due:\n")
        for x in range(0, len(over)):  # This will get index value for list over
            for y in range(0, len(accounts)):  # This will get index value for list accounts
                try:
                    count = accounts[y][0][:-1]
                    if count == over[x][0]:
                        print(' '.join(accounts[y]))
                except IndexError:
                    pass


main()
