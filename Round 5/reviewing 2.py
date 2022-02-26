"""Vu Tu Phuong Nguyen
Programming 5.5.2

Create the function is_the_list_in_order, which receives a list as a parameter and returns the information on whether the numbers contained by the list are in an ascending order, i.e. is each value in the list always greater or equal to the one preceding it.

Examples of how the function operates when tested in the interactive mode of the Python interpreter:

>>> is_the_list_in_order([37, 42, 43])
True
>>> is_the_list_in_order([42, 37, 43])
False
"""

number = [1, 2, 3, 4, 5]
def is_the_list_in_order(number):
    """ using the flag to check the condition"""

    if len(number) == 0 or len(number) == 1:
        return True
    flag = 0
    sorted(number)
    if number == sorted(number):
        flag = 1
    if flag:
        return True
    else:
        return False
if __name__ == "__is_the_list_in_order__":
    is_the_list_in_order()
