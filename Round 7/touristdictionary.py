"""
COMP.CS.100 Programming 1
Code template for  tourist dictionary.
"""
"""

Getting acquainted with dict structure by implementing a simple dictionary to help a tourist while abroad.
The task has been planned so that it is easy to implement when the dictionary's information is saved in a dict structure.
If you end up adding a list to your program yourself, saving the information contained by the dictionary, you have not understood how dict operates.
The easiest approach is getting acquainted with
the operations of the dict structure and not using the list for saving data.
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: W
Enter the word to be translated: hey
hey in Spanish is hola
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: W
Enter the word to be translated: thanks
thanks in Spanish is gracias
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: W
Enter the word to be translated: welcome
The word welcome could not be found from the dictionary.
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: Q
Adios!


Next, implement the operation A, so that the program operates like this:

[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: A
Give the word to be added in English: welcome
Give the word to be added in Spanish: bienvenida
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: A
Give the word to be added in English: yes
Give the word to be added in Spanish: si
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: W
Enter the word to be translated: welcome
welcome in Spanish is bienvenida
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: W
Enter the word to be translated: yes
yes in Spanish is si
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: Q
Adios!


Also implement operation R, so that the program works like this:

[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: R
Give the word to be removed: hey
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: W
Enter the word to be translated: hey
The word hey could not be found from the dictionary.
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: R
Give the word to be removed: hey
The word hey could not be found from the dictionary.
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: Q
Adios!


When travelling you may get into situation where it is hard to use the computer. Thus, it would be nice if the words in the dictionary could be printed on paper. Implement the command P, which prints all the words contained by the dictionary in an alphabetical order according to the English word as follows:

[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: P
hey hola
home casa
thanks gracias
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: Q
Adios!

Improve the dictionary program by adding the command T, which translates an entire sentence instead of one word. An example of the functioning of the program:

[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: T
Enter the text to be translated into Spanish: my home is your home
The text, translated by the dictionary:
my casa is your casa
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: A
Give the word to be added in English: my
Give the word to be added in Spanish: mi
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: A
Give the word to be added in English: your
Give the word to be added in Spanish: su
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: T
Enter the text to be translated into Spanish: my home is your home
The text, translated by the dictionary:
mi casa is su casa
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: A
Give the word to be added in English: is
Give the word to be added in Spanish: es
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: T
Enter the text to be translated into Spanish: my home is your home
The text, translated by the dictionary:
mi casa es su casa
[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: Q
Adios!

If the word in the translated sentence is not in the dictionary, the
word in question should be printed to the sentence in English.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    convert = list(english_spanish.items())
    convert.sort()
    english_spanish = dict(convert)

    print("Dictionary contents: ")
    for key_dict in english_spanish:
        print(key_dict, end=" , ")
    print()

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

            print("Dictionary contents: ")
            convert = list(english_spanish.items())
            convert.sort()
            english_spanish = dict(convert)
            for key_dict in english_spanish:
                print(key_dict, end=" , ")
            print()

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
