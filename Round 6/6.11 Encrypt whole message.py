"""
COMP.CS.100 Programming 1
Code Template

Implement the final version of the ROT-13 program so that it first reads the encrypted message from the user as a whole (the message is ended by entering an empty row). After this, the message is printed as encrypted. An example of how the program operates:

Enter text rows to the message. Quit by entering an empty row.
Puff, the magic dragon lived by the sea,
And frolicked in the autumn mist, in a land called Honah Lee.

ROT13:
Chss, gur zntvp qentba yvirq ol gur frn,
Naq sebyvpxrq va gur nhghza zvfg, va n ynaq pnyyrq Ubanu Yrr.

"""
def encrypt(text):
    """
    Encrypts its parameter using ROT13 encryption technology.

    :param text: str,  string to be encrypted
    :return: str, <text> parameter encrypted using ROT13
    """

    regular_chars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k",
                     "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
                     "w", "x", "y", "z"]

    encrypted_chars = ["n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x",
                       "y", "z", "a", "b", "c", "d", "e", "f", "g", "h", "i",
                       "j", "k", "l", "m"]


    en_text = ""
    lower = ""
    if text.isupper():
        lower = text.lower()
        if lower in regular_chars:
            for index in range(0, len(regular_chars)):
                if lower == regular_chars[index]:
                    en_text = (encrypted_chars[index]).upper()
        else:
            en_text = lower
    else:
        if text in regular_chars:
            for index in range (0,len(regular_chars)):
                if text == regular_chars[index]:
                    en_text = encrypted_chars[index]
        else:
            en_text = text
    return en_text



def row_encryption(message):
    """separate the alphabet into 2 parts and the middle one is the letter no13
     :param message: string, to make the loop checking if the letter go through the parameter word
      return the value after converting"""
    alphabet = 'abcdefghjiklmnopqrstuvwxyz'
    string = ''
    for i in message:
        #lowercase
        if i in alphabet:
            if alphabet.index(i) < 13:
                string += alphabet[alphabet.index(i) +13]
            else:
                string += alphabet[alphabet.index(i) -13]
        #uppercase
        elif i in alphabet.upper():
            if alphabet.upper().index(i) < 13:
                string += alphabet.upper()[alphabet.upper().index(i) + 13]
            else:
                string += alphabet.upper()[alphabet.upper().index(i) - 13]
        #number and other characters
        else:
            string += i
    return string


def read_message():
    """create the string and let the input string from user be stored in that string
    make a while loop to continue running, only break if input is blank twice"""
    message_list = []
    while True:
        input_message = input()
        if input_message == "":
            break
        message_list.append(input_message)
    return message_list

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    passage = read_message()
    print("ROT13: ")
    for lines in passage:
        complete_message = row_encryption(lines)
        print(complete_message)
if __name__ == "__main__":
    main()
