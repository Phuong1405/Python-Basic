"""Vu Tu Phuong Nguyen
Programming 1

Create a program that reads a file and prints its contents with each row starts with the row's number and a space.

For instance, when the text inside text.txt is:

Yogi has a best friend too
Boo Boo, Boo Boo
Yogi has a best friend too
Boo Boo, Boo Boo Bear
Boo Boo, Boo Boo Bear
Boo Boo, Boo Boo Bear
Yogi has a best friend too
Boo Boo, Boo Boo Bear
the program should work like this:

Enter the name of the file: text.txt
1 Yogi has a best friend too
2 Boo Boo, Boo Boo
3 Yogi has a best friend too
4 Boo Boo, Boo Boo Bear
5 Boo Boo, Boo Boo Bear
6 Boo Boo, Boo Boo Bear
7 Yogi has a best friend too
8 Boo Boo, Boo Boo Bear
Programming tips:


A text file read in Python should be located in the PyCharm project folder, ie. the location of the program code file.
You should also note that PyCharm is a text editor, so you can create .txt files using PyCharm.

Remember that the processing of the file in Python consists of three steps:

1.Opening the file

2.Reviewing its contents

3.Closing the file

The solution for this task must thus contain these three parts in this order.

To increase the row numbers when printing, your program needs a variable that calculates which row is being processed. Add the printing of this variable (and a space) to the same command as the one where you print the row containing the file on screen.

If you get extra empty lines in your output, review rstrip method for removing invisible word separator characters from the the end of a string."""

def main():
    file_name = input("Enter the name of the file: ")
    file = open(file_name, mode = "r")

    counter = 1
    for reader in file:
        counter +=1
        file_line = reader.rstrip()
        print(f"{counter-1} {file_line}")
    file.close()


if __name__ == "__main__":
    main()
