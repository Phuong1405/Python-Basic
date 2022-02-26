"""VU TU PHUONG NGUYEN
PROGRAMMING 1 spring 2021

Implement the function count_abbas, which returns the number of abbas
(meaning the string "abba") that the parameter string contains.

Example of how the function operates,
when tested in the interactive mode of the Python interpreter (PyCharm's Python console):

>>> count_abbas("abbabbabba")
3
>>> count_abbas("barbapapa")
0
"""
def count_abbas(word):
    """the condition is correct then finding the "abba" in the parameter word
    param: string
    return count where index more than 0 will run the loop again"""
    count = 0
    index = 0

    while True:
        index = word.find('abba',index)
        if index >= 0:
            count += 1
            index += 1
        else:
            break
    return count

def main():
    count_abbas('abbabbabba')

if __name__ == "__main__":
    main()
