
"""Vu Tu Phuong Nguyen
Programming 1

At one point in the past a decision was made, due to a difficult situation in the world, that the students would not have to take final exams at the end that semester. Anyone who would get a grade 1–5 based on their exercise points would instead have a final grade pass without having to take the exam as per the usual requirement.

Your job is to implement a function named convert_grades which helps the teachers to manage this difficult process of modifying the grades.
This function should receive a list on integers between 0–5 as its parameter. Each of these numbers represent an unmodified grade for an individual student. Your function is to loop over the numbers in the parameter list and replace every grade greater than zero with the value 6, which is/was the number used to express grade "pass" in the student database. Your function must not return a value nor is allowed to print anything on the screen.

To implement convert_grades function you can use the code template here. You should note in the template how convert_grade does not have a return value. It instead relies on the fact, that by modifyind the list it receives as a parameter, it can change the value of the actual parameter grade.

The automatic tests for this assignment are all programming style checks, and unit tests which will check the following details in your program:

convert_grades modifies its parameter list as required,
it does not have a return value,
it does not print anything on the screen and
it does not read any user input from the keyboard.
You can use the provided main function to test your program. The automatic tests don't pay any attention to what main does. You can even leave it out of your submission if you so wish.

Remember handle the speacial case when the parameter list is empty. In that case convert_grades doesn't need to do anything.
"""



def convert_grades(number):
    """
    print grades with new reference value of 6 for every number greater
    than 0 to define it as pass
    """
    for i in range(len(number)):
        if number[i] > 0:
            number[i] = 6

def main():
    grades = [0, 1, 0, 2, 0, 3, 0, 4, 0, 5, 0]
    convert_grades(grades)
    print(grades)  # Should print [0, 6, 0, 6, 0, 6, 0, 6, 0, 6, 0]


if __name__ == '__main__':
    main()
