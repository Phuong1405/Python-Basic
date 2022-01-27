"""
COMP.CS.101 Programming 1
Print a box with input error checking
"""
def read_input(prompt):
    """
    give the condition in read_input
    """
    answer = -1
    while answer <= 0:
        answer = int(input(prompt))

    return answer

def print_box(width, height, char):
    """print_box function starts with paramater to set the calculation"""
    for line in range (height):
        print(width * char)

def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()
    print_box(width, height, mark)


if __name__ == "__main__":
    main()
