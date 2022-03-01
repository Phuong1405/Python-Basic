"""Vu Tu Phuong Nguyen
Programming 1

Create a program that helps you add up the scores that various contestants have obtained in a game.
The scores are stored in a text file that the program uses as input.
The scores can be entered to the file in practically any order, and the program does not even take a stand on
how many scores each contestant gets. The only operations the program performs are the calculation of the sum of scores of the contestants with the same name and
printing the scores of all the contestants in alphabetical order,
according to the player's name.

If the project folder contains the file game.txt with the following content:

essi 5
pietari 9
essi 2
pietari 10
pietari 7
aps 25
essi 1
The program works like this:

Enter the name of the score file: game.txt
Contestant score:
aps 25
essi 8
pietari 26
Programming tips:

You don't have to handle the errors related to the file handling in this assignment (they will be taken care in the next one).
Before you select a data structure for storing the data from the file, consider the requirements set to the data structure carefully.
The contestant names are printed on the list in an alphabetical order. Each name is related to a score.
If you have selected a suitable data structure, the actual operations of the program (calculating the sum of one contestant and printing the list in an alphabetical order)
can be implemented with a minimal effort.
"""


def main():
    file_name = input("Enter the name of the score file: ")
    file_save = open(file_name, mode="r")
    print("Contestant score: ")
    file_lines = file_save.readlines()
    dictionary = {}
    for line in file_lines:
        #line = line.rstrip()
        #key and value with split will make the separate list value
        key, value = line.split()

        if key in dictionary:
            dictionary[key] += int(value)
        else:
            dictionary[key] = int(value)

    for i in sorted(dictionary):
        print(i, dictionary[i])

    file_save.close()

if __name__ == "__main__":
    main()


