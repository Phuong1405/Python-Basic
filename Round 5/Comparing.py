"""Vu Tu Phuong Nguyen
Programming 5.5.1

Create the function are_all_members_same, which uses a list as a parameter and returns information on whether all the members contained by the list are the same.

Examples of how the function operates, when tested in the interactive mode of the Python interpreter:

>>> are_all_members_same([42, 42, 42, 43, 42])
False
>>> are_all_members_same([42, 42, 42, 42])
True"""

def  are_all_members_same(number):
    """take the parameters as list of numbers"""
    return all(x == number[0] for x in number)


if __name__ == "__are_all_members_same__":
    are_all_members_same()
