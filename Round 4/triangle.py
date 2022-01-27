"""
        In other words, write it inside triple quotes like this
        and place it right in the beginning of your program file.
        Initial comment should explain who wrote the program and
        what does it do.
        """
def calculate_angle(a1,a2 = None):
    """a1 is angle 1
    a2 is angle 2
    it will return the result after 180 - a1 - a2 """
    if a2 == None:
        return int(180 - 90 - a1)
    return int(180 - a1 - a2)



