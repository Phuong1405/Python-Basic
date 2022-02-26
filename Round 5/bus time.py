"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.

Let's assume that at some less inhabited area (Teisko?), buses leave for Tampere according to the following schedule:

6:30
10:15
14:15
16:20
17:20
20:00
Design and implement a program which asks the user what time it is and prints the times for the next three buses, based of the entered time.

To be able to concentrate on the essential matter (presenting the schedule as a list), simplify the presentation of the time by saving the time as one integer where the minutes and the hours are expressed in the same number, i.e. 6:30 as 630 and 16:20 as 1620. Times presented this way can easily be compared with each other (i.e. does a certain time come before another time) using the normal comparison operators. Examples of how the program functions:

Enter the time (as an integer): 1000
The next buses leave:
1015
1415
1620
In the next example notice, how the program must be able to cope if the day changes:

Enter the time (as an integer): 1800
The next buses leave:
2000
630
1015

        """

def main():
    time_table = [630,1015,1415,1620,1720,2000]
    now = int(input("Enter the time (as an integer): "))

    print("The next buses leave:")
    index = 0
    while index < len(time_table):

        if time_table[index] >= now:
            break
        index += 1
        if index >= len(time_table):
            index = 0
            break
    for possible_bus_index in range (index, index + 3):
        print(time_table[possible_bus_index % len(time_table)])


if __name__ == '__main__':
    main()
