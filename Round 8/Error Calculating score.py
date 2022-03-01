"""Vu Tu Phuong Nguyen
Programming 1


Add handling of the error situations to the program you implemented in the previous task.

If the file can not be opened in the read mode, the program prints the error message:

There was an error in reading the file.
If the file contains a line that doesn't consist of two strings separated by (a) space character(s), the program prints the error message:

There was an erroneous line in the file:
and the content of the erroneous line will be printed in the following line.

If the file contains a line where the second string can not be interpreted as an integer value, the program prints the error message:

There was an erroneous score in the file:
and the string that couldn't be interpreted as an integer will be printed in the following line.

The file will be processed line by line from the beginning towards the end.
The program will print the error message related to the first error it finds.
The execution of the program will end immediately after printing the first error message.
This means, that if there are multiple errors in the file, only the first one will be reported. If there is an error in the file,
the program only prints the error message.
"""

def main():
    file_name = input("Enter the name of the score file: ")

    try:
        file_save = open(file_name, mode="r")

    except OSError:
        print("There was an error in reading the file.")
        return

    for line in file_save:
        line = line.rstrip()
        try:
            key, value = line.split()
        except ValueError:
            print("There was an erroneous line in the file: ")
            print(line)
            return

        try:
            value = int(value)
        except ValueError:
            print("There was an erroneous score in the file: ")
            print(value)
            return

if __name__ == "__main__":
    main()

