"""VU TU PHUONG NGUYEN
Programming 1
6.6.1 Reverse the name to correct order

In various lists of names, names are sometimes presented in reverse order, the last name before the first name, so that there is a comma after the last name. Create a function reverse_name, which changes a string containing such a name to the order, where the first name is followed with the last name. The names are separated with a space and the comma as well as all unnecessary spaces are removed. The function returns the modified name.

It is assumed that the name string contains no more than one comma and that the caller of the function always passes at least one character as a parameter value (an empty string "" cannot be a parameter value).

Examples of how the function operates, when tested in the interactive mode of the Python interpreter:

>>> reverse_name("Techie, Teddy")
'Teddy Techie'
>>> reverse_name("Scumble,    Arnold")
'Arnold Scumble'
>>> reverse_name("Fortunato,Frank")
'Frank Fortunato'
>>> reverse_name("von Grünbaumberger, Herbert")
'Herbert von Grünbaumberger'
>>> reverse_name("   Duck,     Donald  ")
'Donald Duck'
The program must take care of special cases, where either the first of the last name has been forgotten, but the comma has been given. In these cases, only the first or the last name is returned without the comma and unnecessary spaces. Examples of function calls in the interactive Python interpreter:

>>> reverse_name("X,")
'X'
>>> reverse_name(",X")
'X'
>>> reverse_name(" , Y ")
'Y'
If the name does not contain a first name nor a last name (it is just a comma), an empty string "" is returned.

It is assumed that the name is correct and the name is returned as such, if it does not contain a comma. Examples of function calls in the interactive Python interpreter:

>>> reverse_name("Stuart Student")
'Stuart Student'
>>> reverse_name("Mando")
'Mando'"""

def reverse_name(name):
    """
    there will be 4 parts:
        last,first => reverse into first last
        last, (blank) => last
        (blank), first => first
        last first => last first
    There is also the string, so there will need to remove the string and the blank
    :param name: str, empty space or string
    :return:
    """
    list_name = name.split(",")

    if len(list_name) == 1:  # in the text there is no comma
        full_name = list_name[0].strip()
        result = f'{full_name}'
        return result

    elif list_name[0] == '' or list_name[1] == '':
        list_name.remove('')
        full_name = list_name[0].strip()
        result = f'{full_name}'
        return result

    elif list_name[0] == ' ' or list_name[1] == ' ':
        list_name.remove(' ')
        full_name = list_name[0].strip()
        result = f'{full_name}'
        return result

    else:
        full_name = list_name[1].strip() + " " + list_name[0].strip()
        result = f'{full_name}'
        return result

if __name__ == "__reverse_name__":
    reverse_name()
