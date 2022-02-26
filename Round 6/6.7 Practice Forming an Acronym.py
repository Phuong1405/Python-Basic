"""VU TU PHUONG NGUYEN
PROGRAMMING 1 spring 2021

Implement the function create_an_acronym, which requests a name as a parameter and returns its acronym.
An acronym is formed by taking the first letter of every word in a name and capitalizing it.

It is assumed that the caller of the function always passes at least one character as a parameter value
(an empty string "" cannot be a parameter value).

Example of how the function operates, when tested in the interactive mode of the Python interpreter
(PyCharm's Python console):

>>> create_an_acronym("central intelligence agency")
'CIA'
"""

def create_an_acronym(name):
    """set the blank string to start the loop. the condition continues when i is from 1 to len(string)
        :param name:
        :return: text in upper case
        """
    text = name[0] #add the first letter of string to output
    #text is the index 0 of the "name" string
    # adding the first letter
    for i in range(1, len(name)):
    #loop "i" running through all the "name" string (iterate over the full string and add every next letter to space to output)
        if name[i - 1] == ' ': #condition to choose only the first letter in each word
        #if that index - 1 = there is space before that
        #' ' to set all the CIA
            text += name[i]
    text = text.upper()
    return text
if __name__ == "__create_an_acronym__":
    create_an_acronym()
