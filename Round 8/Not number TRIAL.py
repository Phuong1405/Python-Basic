"""Vu Tu Phuong Nguyen
Programming 1

Implement a program that reads an user message in the usual style, ending with an empty line,
and then saves it to a file so that the file also contains line numbers, as in the earlier assignment.
Finally, the program should print an announcement of the file being written or, alternatively,
an announcement that writing to the file did not succeed.

Enter the name of the file: yogi.txt
Enter rows of text. Quit by entering an empty row.
I know someone you don't know
Yogi, Yogi

File yogi.txt has been written.
After this, the file yogi.txt shows up in the project folder, with the contents:

1 I know someone you don't know
2 Yogi, Yogi
If opening the output file fails, the following error message should be printed immediatelly:

Writing the file yogi.txt was not successful.
where yogi.txt should be replaced with the file name entered by the user.

The file is opened for writing even before the text written to file was asked from the user.
This way, the error message is printed to the user and the program ended before asking the text, meaning the user does not need to write any text needlessly.


Programming tips:

Use the function read_message implemented in the task saving a message (6.10). The function in question forms a list
that contains the rows of the message written by the user.

As this task processes the file, it also creates a solution
which contains the same three phases as the first file-processing program, so remind yourself what these phases are.

Program differences in section a:

The opening of the file must define writing, instead of reading, as the way of processing.
The for command reviews the list returned by the input reading function,
and every string contained by the list is entered to the open file using a write method.
The closing of a file happens just like the closing of the file being read.

The errors in writing the file can be processed using an exception, just like the errors in reading the file.
"""

def read_message():
    """Make the loop for leave a blank input"""
    message_list = []
    while True:
        text_line = input()

        if text_line == "":
            break
        message_list.append(text_line)
    return message_list

def main():
    filename = input("Enter the name of the file: ")
    try:
        save_file = open(filename, mode="w")

    except OSError:
        print(f"Writing the file {filename} was not successful.")
        return
    print("Enter rows of text. Quit by entering an empty row.")
    message = read_message()
    counter = 0
    for lines in message:
        counter += 1
        print(counter, lines, file=save_file)
    print(f"File {filename} has been written.")
    save_file.close()



if __name__ == "__main__":
    main()
