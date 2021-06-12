"""
    Read files into python and use the file content with parallel lists
"""


def main():
    print("We can help decode a text file of your choice.")
    prompt = input("What is the file name that you want to decode? ")
    decoded_msg = ''
    try:
        file = open(prompt, 'r')
        line = file.readline().strip('\n')
        while line != '':
            decoded_msg += line
            line = file.readline().strip('\n')
        file.close()
    except IOError:
        print(f"Sorry the file {prompt} does not exist.")
    print(morse_decoder(decoded_msg))


def morse_decoder(x):
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

    phrase = x.split()
    secret = ''
    for words in phrase:
        for y in range(0, len(abc)):
            if words == morse[y]:
                secret += abc[y]
    return secret


main()
