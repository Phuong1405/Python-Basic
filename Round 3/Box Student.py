"""
       In other words, write it inside triple quotes like this
       and place it right in the beginning of your program file.
       Initial comment should explain who wrote the program and
       what does it do.
       """

def print_box(columns, lines, character):
    """print_box is a function to call the columns, lines and characters"""
    for line in range(lines):
        for column in range (columns):
            print(character, end="")
        print()

def main():
    columns = int(input("Enter the width of a frame: "))
    lines = int(input("Enter the height of a frame: "))
    character = input("Enter a print mark: ")
    print()

    print_box(columns, lines, character)

if __name__ == "__main__":
    main()