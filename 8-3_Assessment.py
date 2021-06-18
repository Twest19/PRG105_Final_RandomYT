"""
    Match strings in a list
    Error Checking
    Download both files: accounts.txt over90.txt
    Read both files into lists. Print the complete customer information on the screen if they are on both lists.
    Do error checking for file names to make sure the files exist (try and except statements.)
"""


def main():
    file_one = open('accounts.txt', 'r')
    lines = file_one.readlines()
    accounts = []
    for line in lines:
        x = line.split()
        accounts.append(x)
    file_one.close()

    file_two = open('over90.txt', 'r')
    num = file_two.readlines()
    over = []
    for n in num:
        y = n.split()
        over.append(y)
    file_two.close()

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
