"""Vu Tu Phuong Nguyen
Programming 5.2.1

Create a program that first reads 5 numbers a user enters and then prints,
in the order the user entered them, all the numbers that are greater than zero. An example of how the program operates:

Give 5 numbers:
Next number: 0
Next number: 1
Next number: -2
Next number: 3
Next number: -4
The numbers you entered that were greater than zero were:
1
3


"""

def main():
    list_number = []
    print("Give 5 numbers: ")

    for i in range(0,5):
        i = int(input("Next number: "))
        list_number.append(i)
    print("The numbers you entered that were greater than zero were:")
    for a in list_number:
        if a > 0:
            print(a)



if __name__== "__main__":
    main()
