"""
COMP.CS.101 Programming 1
Assignment "Improved Box Printing" code template
"""

# TODO: the definition of print_box goes here unless it goes after main.

def main():
    print_box(5, 4)
    print("")
    print_box(3, 8, "*")
    print("")
    print_box(5, 4, "O", "o")
    print("")
    print_box(inner_mark=".", border_mark="O", height=4, width=6)

def print_box(width, height, border_mark="#", inner_mark=" "):
    """print_box calculate the presence of mark"""
    print(width * border_mark)
    for linenum in range (height - 2):
            print(border_mark, (width-2) * inner_mark, border_mark, sep="")
    print(width * border_mark)


# TODO: the definition of print_box could also go here, it is up to you.


if __name__ == "__main__":
    main()
