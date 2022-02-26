"""Vu Tu Phuong Nguyen
Programming 5.2.1


Create a program that first reads 5 numbers a user has entered and then prints all the entered numbers in reverse order. An example of how the program operates:

Give 5 numbers:
Next number: 2
Next number: 7
Next number: 3
Next number: -8
Next number: 6
The numbers you entered, in reverse order:
6
-8
3
7
2


Programming Tips
When you printed the numbers in a list in the previous assignment,
the for loop processed the values saved in the list directly
(at least if you implemented it in the simplest way).
In this task, the list must be gone through in reverse order during
the printing phase. This can not be done with a simple for loop, but rather,
the user must use list indexes.

These indexes are the ordinal numbers for the list's elements, which can be used to access the members of the list using the indexing operator listname[index].
To implement this program, write a for loop,
which goes through the list's indexes in the order
you want the printing to happen (from the largest to the smallest).
Then, in the body of this for loop, you can access
the value in the list by indexing it with the loop variable.

"""

def main():
    list_number = []
    print("Give 5 numbers: ")

    for i in range(1, 6):
    #for i in range (0,5)
        i = int(input("Next number: "))
        list_number.append(i)
    print("The numbers you entered, in reverse order: ")
    list_number.reverse()
    for a in list_number:
        print(a)

    #for a in range(len(list_number)-1,-1,-1):
    #    print(list_number[a])




if __name__== "__main__":
    main()
