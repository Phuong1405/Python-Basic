"""
COMP.CS.100 Programming 1
Code Template

Implement the function longest_substring_in_order,
which takes a string as its parameter and searches for the longest substring with its characters in alphabetic order and then returns it. You can assume the string contains only lower-case letters, so you can compare the alphabetical order of the strings by using the comparison operator <, for instance.

If the string contains several equally long substrings in alphabetic order,
the program returns the substring that is the closest to the beginning of the string.

The function returns its parameter value, if it is an empty string "" or a string made of a single character.

The longest substring in alphabetical order is character x,
for strings that consist only of occurrences of x and x has at least two occurrences. For example, if the parameter value is "aaa", the return value is "a".

Example of how the function operates, when tested in the interactive mode of the Python interpreter (PyCharm's Python console):

>>> longest_substring_in_order("abcabcdefgabab")
'abcdefg'
>>> longest_substring_in_order("acdkbarstyefgioprtyrtyx")
'efgioprty'
"""
def longest_substring_in_order(string):
    """:param string: checking the list of the letter"""

    longest = ""
    max =""

    for i in range(len(string) - 1):
        if(string[i] <= string[i+1]):
           longest = longest + string[i]
           if(i==len(string) -2):
               longest = longest + string[i+1]
        else:
            longest  = longest + string[i]
            if(len(longest) > len(max)):
                max = longest
            longest = ""

    if(len(string) == 1):
        longest = string

    if(len(longest) > len(max)):
        return longest
    else:
        return max

if __name__ == '__longest_substring_in_order__':
    longest_substring_in_order()
