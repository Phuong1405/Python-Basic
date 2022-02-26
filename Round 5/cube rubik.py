"""Vu Tu Phuong Nguyen
Programming 5.5.1

In official Rubik's Cube contests, a participant's score is evaluated in the following way:

The contestant may solve the Rubik's Cube five times. Each achievement time is measured in seconds.
The best and the worst time are removed.
An average of the remaining times is calculated and set as the contestant's official score.
Implement a program that asks for the times of the contestant's performances and prints the result to the hundredth of a second. An example of how the program functions:

Enter the time for performance 1: 5.80
Enter the time for performance 2: 5.40
Enter the time for performance 3: 5.17
Enter the time for performance 4: 5.19
Enter the time for performance 5: 5.22
The official competition score is 5.27 seconds.
"""


def main():

    list_number = []
    repetition = 1
    while repetition <= 5:
        number = float(input(f"Enter the time for performance {repetition}: "))
        repetition += 1
        list_number.append(number)


    min_number = min(list_number)
    list_number.remove(min_number)

    max_number = max(list_number)
    list_number.remove(max_number)

    average = sum(list_number)
    print(f"The official competition score is {average:.2f} seconds.")

if __name__ == "__main__":
    main()
