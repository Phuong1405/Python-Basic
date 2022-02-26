"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.

mplement the function calculate_angle, that will calculate (and return!) the magnitude of the third angle of the triangle,
when the magnitudes of the other two angles are known (i.e. given as parameters to the function).
The function must handle right-angled triangle as an exception. In case of a right-angled triangle you don't need to give the magnitude of the right-angle (90°) as a parameter at all: the function only needs the magnitude of one of the sharp angles as a parameter and will calculate the magnitude of the other sharp angle.

Please, note that in this task the main function is optional.
Plussa tests only that the calculate_angle function has been defined correctly. You can use either the main function or the Python console to test your function, before submitting the solution. An example of how the function operates, when tested in the Python console (In interactive mode, the Python interpreter automatically prints the return value of the function to the screen.):


>>> calculate_angle(50, 60)
70
>>> calculate_angle(30)
60
>>>

        """
def calculate_angle(a1,a2 = None):
    """a1 is angle 1
    a2 is angle 2
    it will return the result after 180 - a1 - a2 """
    if a2 == None:
        return int(180 - 90 - a1)
    return int(180 - a1 - a2)



