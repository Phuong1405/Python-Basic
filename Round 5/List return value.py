"""Vu Tu Phuong Nguyen
Programming 5.4.1

Create a function named input_to_list which has 1 parameter: number of integers user needs to enter. The function then asks user to enter that many numbers, reads the numbers from the user, saves them in a list and returns that list.

Also create a main function which:

asks the user for the number of integers to be processed
calls input_to_list to read the numbers from the user
asks the user what number the user are searching for and
prints data on whether the searched numbers are found from the entered numbers and, if so, how many times
Examples of how the program works (rows 2–7 are handled by the function):

1
2
3
4
5
6
7
8
9
How many numbers do you want to process: 5
Enter 5 numbers:
7
3
2
7
7
Enter the number to be searched: 7
7 shows up 3 times among the numbers you have entered.
In the next example lines 2–5 happen in input_to_list:

1
2
3
4
5
6
7
How many numbers do you want to process: 3
Enter 3 numbers:
5
6
7
Enter the number to be searched: 3
3 is not among the numbers you have entered."""

def input_to_list (number):
    """determine the input numbers"""
    list_number = []
    for i in range (number):
        number = int(input())
        list_number.append(number)
    return list_number

def main():

    round = int(input("How many numbers do you want to process: "))
    print(f"Enter {round} numbers: ")

    name = input_to_list(round)
    searched_number = int(input("Enter the number to be searched: "))
    counting = name.count(searched_number)
    if counting > 0:
        print(f"{searched_number} shows up {counting} times among the numbers you have entered.")
    else:
        print(f"{searched_number} is not among the numbers you have entered.")


if __name__== "__main__":
    main()
