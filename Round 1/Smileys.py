"""Create a program that asks the user how they feel on scale 1-10 and
then proposes a suitable emoticon to describe the mood.
First implement a relatively expressionless version that prints :-)for feelings over 7
and otherwise prints the basic face :-|.

Examples of how the program works:

    How do you feel? (1-10) 6
    A suitable smiley would be :-|
    and

How do you feel? (1-10) 9
A suitable smiley would be :-)
You can return this task for the first time at this phase.
An automatic evaluation offers a partial score for each subsection.
You receive a full score when every subsection operates correctly.

Now make the previously mentioned program verify the numeric values -
if something other than a numeric value between 1 and 10 is entered,
the program should print Bad input!

Otherwise, the program should operate like in section a),
but an example of an error of this sort would be:

    How do you feel? (1-10) 42
    Bad input!

You should be able to express negative emotions when necessary,
so let’s add the program a sad emoticon :-(,
which is recommended for feelings that are less than 4.

Let’s add more expressiveness to the program.
The extremes of the emotion scale,
the values 1 and 10, use the stronger faces :'( and :-D.
"""


def main():
    value = int(input("How do you feel? (1-10) "))


    if 1 <= value <= 10:
     if value >= 4 and value <= 7:
        print("A suitable smiley would be :-|")
     elif 7 < value < 10:
        print("A suitable smiley would be :-)")
     elif 1 < value < 4:
        print("A suitable smiley would be :-(")
     elif value == 1:
        print("A suitable smiley would be :'(")
     elif value == 10:
        print("A suitable smiley would be :-D")

    else:
        print("Bad input!")



if __name__ == '__main__':
    main()
