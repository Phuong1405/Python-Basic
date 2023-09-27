def print_matrix(matrix, column_width):
    """Prints a matrix represented as nested lists to the screen. The rows
    of the matrix can be of different lengths. The parameter values are
    assumed to be valid.

    :param matrix: list, a matrix as a list of lists having integer elements.
    Sublists contain the rows of the matrix.
    :param column_width: int, the width of each column in characters.
    """

    # Print the matrix row by row.
    for row in matrix:
        # Print elements on the same line. Space is printed depending of
        # the column: The separating space is omitted, when the first column
        # is printed.
        first_column = True
        for element in row:
            if first_column:
                print(f"{element:{column_width - 1}}", end="")
                first_column = False
            else:
                print(f"{element:>{column_width}}", end="")

        # Start a new line only after all of the elements of the row have
        # been printed.

if __name__ == "__print_matrix__":
    print_matrix()