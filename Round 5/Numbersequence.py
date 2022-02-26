"""Vu Tu Phuong Nguyen
Programming 5.2.1

Create a program that first prints the even numbers from 0 to 100
in an ascending order, and then the same numbers in descending order.
Each number is printed on its own row,
so the program's printout looks like this:

0
2
4
6
⋮
98
100
100
98
⋮
4
2
0"""

def main():
    for number in range (0,101,2):
        print (number)
    for number in range (100,-1,-2):
        print (number)








if __name__== "__main__":
    main()
