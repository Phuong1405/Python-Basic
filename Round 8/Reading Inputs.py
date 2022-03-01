"""Vu Tu Phuong Nguyen
Programming 1

In the assignment printing a box and checking the inputs we implemented a function read_input
that read a user's input and checked that the entered number was positive. The task in question did not check, however,
that the input was otherwise valid, ie. entering letters made the program crash.
Let's fix the function read_input so that it also asks the input again when the user enters something other than an integer.

Take your submission to the previous task as the basis of your solution,
and add checking for incorrect entries to the error checks used in the function read_input. The program should work like this:

Enter the width of a frame: hey
Enter the width of a frame: hello
Enter the width of a frame: jep
Enter the width of a frame: 5
Enter the height of a frame: wut
Enter the height of a frame: what
Enter the height of a frame: *
Enter the height of a frame: mordor
Enter the height of a frame: 10
Enter a print mark: M

MMMMM
MMMMM
MMMMM
MMMMM
MMMMM
MMMMM
MMMMM
MMMMM
MMMMM
MMMMM



Programming tips:

Use a try-except structure to detect errorneous inputs. The try block should be kept as small as possible. Consider carefully, which of the code lines need to be inside the try block and which not."""

def read_input(prompt):
    """to check the condition of the of the width and height
       :param:prompt: int, input the suitable number
        """
    if prompt == "Enter the width of a frame: ":
        while True:
            try:
                prompt = int(prompt)
                break
            except:
                prompt = input("Enter the width of a frame: ")

    if prompt == "Enter the height of a frame: ":
        while True:
            try:
                prompt = int(prompt)
                break
            except:
                prompt = input("Enter the height of a frame: ")

    return prompt


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    for line in range(height):
        for column in range (width):
            print(mark, end="")
        print()


if __name__ == "__main__":
    main()
