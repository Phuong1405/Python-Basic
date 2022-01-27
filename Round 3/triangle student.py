"""
s = (a+b+c)/2

dien tich = Can bac 2(s.(s-a).(s-b).(s-c))

An example of how the program operates:

Enter the length of the first side: 2.5
Enter the length of the second side: 3
Enter the length of the third side: 4.5
The triangle's area is 3.5
       
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
