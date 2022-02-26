
"""
COMP.CS.100 Programming 1
ROT13 program code template

Implement a so-called ROT-13 encryption. In ROT-13 system, the characters are replaced with other characters in accordance with the following formula:

unencrypted character:

a b c d e f g h i j k l m n o p q r s t u v w x y z
encrypted character:

n o p q r s t u v w x y z a b c d e f g h i j k l m
Upper-case letters are changed to other upper-case letters using the same logic. The characters that were not listed in the previous table are maintained as they are. For instance the string:

Happy, happy, joy, joy!
would be the following when encrypted in ROT-13:

Unccl, unccl, wbl, wbl!
Note that if the ROT-13 encryption is performed twice, first for the original text and then for the encrypted text, you will receive the original message in non-encrypted format. This can also be utilized in testing the program.


a) encrypt function
First, we shall review the use of lists. Using the attached template , first implement the function encrypt, which performs the ROT13 transformation for one character. This means the function uses one character as its parameter and returns the encrypted character that matches the character in question.

You may assume that the parameter is always a character, i.e., a string consisting of a single character.

Example of how the function operates, when tested in the interactive mode of the Python interpreter (PyCharm's Python console):

>>> encrypt("e")
'r'
>>> encrypt("E")
'R'
>>> encrypt("?")
'?'


b)row_encryption function
Implement a new function, row_encryption,
which perfoms a ROT13 transformation for an entire string.
In other words, this function uses a string as a parameter and
returns a string.

The function returns an empty string, if the parameter value is an empty string.

Example of how the function operates,
when tested in the interactive mode of the Python interpreter
(PyCharm's Python console):

>>> row_encryption("Happy, happy, joy, joy!")
'Unccl, unccl, wbl, wbl!'

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


def row_encryption(word):
    """separate the alphabet into 2 parts and the middle one is the letter no13
     :param word: string, to make the loop checking if the letter go through the parameter word
      return the value after converting"""
    result = ""

    # Loop over characters.
    for letter in word:
        # Convert to number with ord.
        convert = ord(letter)

        # Shift number back or forward.
        if convert >= ord('a') and convert <= ord('z'):
            if convert > ord('m'):
                convert -= 13
            else:
                convert += 13
        elif convert >= ord('A') and convert <= ord('Z'):
            if convert > ord('M'):
                convert-= 13
            else:
                convert += 13
        # Append to result.
        result += chr(convert)

    # Return transformation.
    return result


def main():
    first_result = encrypt("E")
    print(first_result)
    second_result = row_encryption('The quick brown fox jumps over the lazy dog.')
    print(second_result)


if __name__ == '__main__':
    main()
