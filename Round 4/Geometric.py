"""
COMP.CS.100 Programming 1
Code template for geometric patterns.

a) that prompts the user to select a geometric pattern (a square or a rectangle) and to enter the required dimensions. The program prints the circumference and area of the pattern to two decimal places. The program first prints a menu where the user can select their desired pattern or stop the program
(s = square, r = rectangle and q = quit).
This is the menu where the user returns after performing the previously selected action.

If something other than n, s or q is entered, the program prints error message "Incorrect entry, try again!" and returns to the pattern selection. If a negative number or a zero is entered as a dimension, the user is asked to re-enter the value,
using the same prompt as originally.

Enter the pattern's first letter or (q)uit: s
Enter the length of the square's side: 2.2
The circumference is 8.80
The surface area is 4.84

Enter the pattern's first letter or (q)uit: r
Enter the length of the rectangle's side 1: -4
Enter the length of the rectangle's side 1: 1.5
Enter the length of the rectangle's side 2: -3.5
Enter the length of the rectangle's side 2: 2.5
The circumference is 8.00
The surface area is 3.75

Enter the pattern's first letter or (q)uit: y
Incorrect entry, try again!

Enter the pattern's first letter or (q)uit: s
Enter the length of the square's side: 0
Enter the length of the square's side: -3
Enter the length of the square's side: 4
The circumference is 16.00
The surface area is 16.00

Enter the pattern's first letter or (q)uit: q
Goodbye!

Plan how to divide the implemented program into functions.
Invent descriptive names for functions and use one sentence to tell what each function does.
Enter this description in a docstring comment in the beginning of the function.
Comment in the docstring also also the parameter values and the return value of the function.


b)
Add to the program a new geometric pattern: a circle.
The circle is selected from the menu with the c command.
Enter the pattern's first letter or (q)uit: c
Enter the circle's radius: 1.5
The circumference is 9.42
The surface area is 7.07

Enter the pattern's first letter or (q)uit: q
Goodbye!

Earlier we have learned to use ready functions from the mathematic library.
The math library also contains some mathematical constants. If you add line "from math immport pi"
in the beginning of your program you can use the name pi to access the approximate value of π
.

Another prossibility is to just add "import math".
After that you can access the functions and constants of the math library with math.
prefix: math.sqrt(2.0), math.pi etc.

Also consider whether you implemented the previous part's solution in a way
that made it easy to add a new pattern.

"""
from math import pi

#square part
def square_area(side):
    """square area calculation with side is a float"""
    area = side*side
    return area
def square_cir(side):
    """square circumference calculation with side is a float"""
    circumference = 4*side
    return circumference

#rectangle part
def rectangle_area (s1,s2):
    """rectangle circumference calculation with side is a float"""
    area = s1*s2
    return area
def retangle_cir(s1,s2):
    """square circumference calculation with side is a float"""
    circumference = (s1 + s2)*2
    return circumference

#circle part
def circle_area(r):
    """square circumference calculation with side is a float"""
    area = pi* r **2
    return area

def circle_cir(r):
    """square circumference calculation with side is a float"""
    circumference = 2 * pi * r
    return circumference



def menu():
    """
    Print a menu for user to select which geometric pattern to use in calculations.
    """
    main_loop = True
    while main_loop:
        answer = input("Enter the pattern's first letter or (q)uit: ")

        #square
        if answer == "s":
            # Replace this comment and "pass" with your function calls dealing
            # with square.
            side = float(input("Enter the length of the square's side: "))

            while side <= 0:
                side = float(input("Enter the length of the square's side: "))
                if side >= 0:
                    break
            print(f"The circumference is {square_cir(side):.2f}")
            print(f"The surface area is {square_area(side):.2f}")
            print()


        #rectangle
        elif answer == "r":
        # Replace this comment and "pass" with your function calls dealing
        # with rectangle.
            side_1 = float(input("Enter the length of the rectangle's side 1: "))
            while side_1 <= 0:
                side_1 = float(input("Enter the length of the rectangle's side 1: "))
            side_2 = float(input("Enter the length of the rectangle's side 2: "))
            while side_2 <= 0:
                side_2 = float(input("Enter the length of the rectangle's side 2: "))

            print(f"The circumference is {retangle_cir(side_1, side_2):.2f}")
            print(f"The surface area is {rectangle_area(side_1, side_2):.2f}")
            print()

        #circle
        elif answer == "c":
            radius = float(input("Enter the circle's radius: "))
            print(f"The circumference is {circle_cir(radius):.2f}")
            print(f"The surface area is {circle_area(radius):.2f}")
            print()

        #quit
        elif answer == "q":
            main_loop = False
            print("Goodbye!")

        else:
            print("Incorrect entry, try again!")
            print()


def main():
    menu()

if __name__ == "__main__":
    main()
