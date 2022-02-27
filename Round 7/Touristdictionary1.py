"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.

Let's add a printout at the start of the tourist dictionary program to make its use easier. As the dictionary already contains three words, the dictionary's user should be informed of this content. The added printout is shown in the following example run:

Dictionary contents:
hey, home, thanks
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: Q
Adios!
To enable the new feature to be tested a little better, add the same printout, after the earlier printouts of the command A:

Dictionary contents:
hey, home, thanks
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: A
Give the word to be added in English: welcome
Give the word to be added in Spanish: bienvenida
Dictionary contents:
hey, home, thanks, welcome
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: A
Give the word to be added in English: beach
Give the word to be added in Spanish: playa
Dictionary contents:
beach, hey, home, thanks, welcome
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: Q
Adios!
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    convert = list(english_spanish.items())
    convert.sort()
    english_spanish = dict(convert)
    wordlist = []
    print("Dictionary contents: ")
    for key_dict in english_spanish:
        wordlist.append(key_dict)
    print(", ".join(wordlist))

    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":
            word_input = input("Enter the word to be translated: ")
            if word_input in english_spanish:
                translate = english_spanish.get(word_input)
                print(f"{word_input} in Spanish is {translate}")
            else:
                print("The word", word_input,
                      "could not be found from the dictionary.")


        elif command == "A":
            word_Eng = input("Give the word to be added in English: ")
            word_Span = input("Give the word to be added in Spanish: ")

            if word_Eng and word_Span != " ":
                english_spanish[word_Eng] = word_Span

            wordlist = []
            print("Dictionary contents: ")
            convert = list(english_spanish.items())
            convert.sort()
            english_spanish = dict(convert)
            for key_dict in english_spanish:
                wordlist.append(key_dict)
            print(", ".join(wordlist))


        elif command == "R":
            # Read the name from the user.
            word = input("Give the word to be removed: ")

            # Remove from the book.
            if word in english_spanish:
                del english_spanish[word]
            # Print an error message.
            else:
                print(
                    f"The word {word} could not be found from the dictionary.")

        elif command == "P":
            convert = list(english_spanish.items())
            convert.sort()
            english_spanish = dict(convert)

            for word in english_spanish:
                print(word, english_spanish[word])

        elif command == "T":
            sent = input("Enter the text to be translated into Spanish: ")

            # joining the dict word found with the string
            phrase = " ".join([english_spanish.get(w, w) for w in sent.split()])
            print(f"The text, translated by the dictionary: \n{phrase}")

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
