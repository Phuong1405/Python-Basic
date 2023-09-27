"""
COMP.CS.100 Programming 1
VU TU PHUONG NGUYEN
"""

def read_file (readfile):
    """ stores the information in a suitable datastructure, and returns this datastructure.
    If the file was read successfully you can then execute search actions in the Python console"""

    file = open("csv", "r")
    dictionary = {}
    for i in file:

        linestrip = i.strip()
        x = linestrip.split(";")

        if x[4] != "":
            dictionary.update{f"{x[0]} ["name"] \n {x[1]}" }

            {x[0] {"name": x[1],
                             "phone": x[2],
                             "email": x[3],
                             "skype": x[4]}})

        else:
            dictionary.update({x[0]: {"name": x[1],
                             "phone": x[2],
                             "email": x[3]}})


if __name__ == "__read_file__":
    read_file()

