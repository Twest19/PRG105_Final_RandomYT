"""
    Using parallel arrays, create a secret code creator.
    Ask the user for text to enter, convert it to the code, and write the code to a text file.
    Include punctuation (. , !), space, upper, and lower case letters
"""


def main():
    abc = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
           'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
           'U', 'V', 'W', 'X', 'Y', 'Z', ' ', ',', '.', '!', '?',
           "'", '"', '=', '+', '-', '$', '@', '1', '2', '3',
           '4', '5', '6', '7', '8', '9', '0']

    morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---',
             '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-',
             '..-', '...-', '.--', '-..-', '-.--', '--..', '/', '--..--', '.-.-.-', '-.-.--', '..--..',
             '.----.', '.-..-.', '-...-', '.-.-.', '-....-', '...-..-', '.--.-.', '.----', '..---', '...--',
             '....-', '.....', '-....', '--...', '---..', '----.', '-----']

    prompt = input("Enter a phrase you would like to translate into morse code: ")
    
    secret_code = []
    for x in prompt:
        for y in range(0, len(abc)):
            if x.upper() == abc[y]:
                secret_code += morse[y]

    print(f"{prompt} in morse code translates to: \n{secret_code}")
    filename = 'secret_code.txt'
    with open(filename, 'w') as new_file:
        for letters in secret_code:
            new_file.write(str(letters) + "\n")
    new_file.close()


main()
