"""
Course: COMP.CS.100 Programming 1 Fall 2021
Name: Vu Tu Phuong Nguyen
Exercise: Round 3 - 3.3.1 Jogging Analyzer


Program starts by asking the user the number of days they want to analyze:

Enter the number of days:
When the user has entered the number of days, the program starts inquiring
the number of kilometers the user jogged in each day:

Enter day X running length:
Where X is a placeholder for the number of the day, starting from 1.

If the user enters zero kilometers in three consecutive days,
the program should print:

You had too many consecutive lazy days!
Then the program should quit without any further output.

When the user has entered jogging data for X days,
the program displays its judgement in one of the following formats.

If the average of the kilometers jogged per day is less than 3.00 kilometers,
the program should print:

Your running mean of Y.YY km was too low!
On the other hand, if the average is 3.00 kilometers or more,
the printout should be:

You were persistent runner! With a mean of Y.YY km.
In both cases above Y.YY is the placeholder for the average of
the jogging distances expressed with two decimals.

Program ends after the printout.

Suitable Average
Enter the number of days: 7
Enter day 1 running length: 3
Enter day 2 running length: 0
Enter day 3 running length: 0
Enter day 4 running length: 7
Enter day 5 running length: 8
Enter day 6 running length: 5.4
Enter day 7 running length: 7.1

You were persistent runner! With a mean of 4.36 km.
Too Little
Enter the number of days: 9
Enter day 1 running length: 3.1
Enter day 2 running length: 2.2
Enter day 3 running length: 1
Enter day 4 running length: 2.8
Enter day 5 running length: 2.3
Enter day 6 running length: 0
Enter day 7 running length: 1.3
Enter day 8 running length: 1.5
Enter day 9 running length: 2.6

Your running mean of 1.87 km was too low!
Too Many Days without Running
Enter the number of days: 10
Enter day 1 running length: 3.3
Enter day 2 running length: 1.2
Enter day 3 running length: 4.2
Enter day 4 running length: 0
Enter day 5 running length: 0
Enter day 6 running length: 0

You had too many consecutive lazy days!
"""
def main():
    day = int(input("Enter the number of days: "))
    repetition = 1
    sum = 0
    counting = 0
    while repetition <= day:
        length = float(input(f"Enter day {repetition} running length: "))
        sum += length
        repetition += 1
        mean = float((f"{sum / day:.2f}"))

        if day == (repetition - 1):
            if mean >= 3.00:
                print()
                print(f"You were persistent runner! With a mean of {mean:.2f} km.")
            if mean < 3.00:
                print()
                print(f"Your running mean of {mean:.2f} km was too low!")
        if length == 0:
            counting += 1
            if counting >= 3:
                print()
                print("You had too many consecutive lazy days!")
                break
        else:
            counting = 0

if __name__ == "__main__":
    main()
