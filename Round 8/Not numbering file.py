"""Vu Tu Phuong Nguyen
Programming 1"""



def main():
    filename = input("Enter the name of the file: ")

    try:
        # To be able to write into file the value of the
        # mode parameter for open must be "w" (write).
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file '{filename}' was not successful.")
        return

    print("Enter rows of text. Quit""")



def main():
    filename = input("Enter the name of the file: ")

    try:
        # To be able to write into file the value of the
        # mode parameter for open must be "w" (write).
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file '{filename}' was not successful.")
        return

    print("Enter rows of text. Quit by entering an empty row:")

    while True:
        text_line = input()

        if text_line == "":
            break

        print(text_line, file=save_file)

    save_file.close()

    print(f"Done! File '{filename}' saved.")



if __name__ == "__main__":
    main()
 by entering an empty row:")

    while True:
        text_line = input()

        if text_line == "":
            break

        print(text_line, file=save_file)

    save_file.close()

    print(f"Done! File '{filename}' saved.")



if __name__ == "__main__":
    main()


print("There was an erroneous line in the file: ")