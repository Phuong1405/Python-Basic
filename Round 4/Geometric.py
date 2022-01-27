"""
COMP.CS.100 Programming 1
Code template for geometric patterns.
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