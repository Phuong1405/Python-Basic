"""
       In other words, write it inside triple quotes like this
       and place it right in the beginning of your program file.
       Initial comment should explain who wrote the program and
       what does it do.
       """
from math import sqrt

def read_float(prompt):
    """the read_float starts the number for returning the value"""
    # if....
    number = float(input(prompt))
    #else:
    return number
def area(a,b,c):
    """the calculate_area gives the return value with the formula"""
    #semiperimeter = (a+b+c)/c
    s = (a + b + c)/2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return area

def main():
    """main function calculate the result and print the result"""
    a = read_float("Enter the length of the first side: ")
    b = read_float("Enter the length of the second side: ")
    c = read_float("Enter the length of the third side: ")

    result = area(a, b, c)
    print(f"The triangle's area is {result:.1f}")

if __name__ == "__main__":
    main()
