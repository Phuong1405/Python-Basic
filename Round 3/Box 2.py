"""
The checks for user inputs in many programs resemble each other.
For instance, in the previously implemented program for printing the box,
it is good to check that the numbers entered by the user are greater than zero. A similar check can also be performed in the program that calculates the area of a triangle.

Use the attached program code template. Add the print_box function
you implemented earlier into the code template.

Implement the function read_input, which reads the number entered by the user,
checks that it is larger than zero, and returns it to
the caller of the function. The function also requests the user to
enter a new input until the user enters a positive number.

The function is used both for asking the width and the height of the box.
Therefore, the string it uses as a prompt when asking for input is passed
as a parameter to the function.

Enter the width of a frame: -1
Enter the width of a frame: 0
Enter the width of a frame: -4
Enter the width of a frame: 4
Enter the height of a frame: -1
Enter the height of a frame: 0
Enter the height of a frame: 2
Enter a print mark: #

####
####
"""
def read_input(prompt):
    """
    give the condition in read_input
    """
    answer = -1
    while answer <= 0:
        answer = int(input(prompt))

    return answer

def print_box(width, height, char):
    """print_box function starts with paramater to set the calculation"""
    for line in range (height):
        print(width * char)

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
