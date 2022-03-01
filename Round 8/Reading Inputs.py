"""Vu Tu Phuong Nguyen
Programming 1"""

def read_input(prompt):
    """to check the condition of the of the width and height
       :param:prompt: int, input the suitable number
        """
    if prompt == "Enter the width of a frame: ":
        while True:
            try:
                prompt = int(prompt)
                break
            except:
                prompt = input("Enter the width of a frame: ")

    if prompt == "Enter the height of a frame: ":
        while True:
            try:
                prompt = int(prompt)
                break
            except:
                prompt = input("Enter the height of a frame: ")

    return prompt


def main():
    width = read_input("Enter the width of a frame: ")
    height = read_input("Enter the height of a frame: ")
    mark = input("Enter a print mark: ")
    print()

    for line in range(height):
        for column in range (width):
            print(mark, end="")
        print()


if __name__ == "__main__":
    main()