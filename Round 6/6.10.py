"""
COMP.CS.100 Programming 1
Code Template

Implement the function read_message to the attached code template .
The function reads the input entered by the user, saves the rows in a list, and returns the list. The entry of the input is terminated by entering an empty row. This empty row is not saved in list.

Also implement a main program that calls the function to read a message
and then prints the strings in the list using ALL CAPITALS.
An example of how the program operates:

Enter the text rows of the message. End by entering an empty row.
Puff, the magic dragon lived by the sea,
And frolicked in the autumn mist, in a land called Honah Lee.

The same, shouting:
PUFF, THE MAGIC DRAGON LIVED BY THE SEA,
AND FROLICKED IN THE AUTUMN MIST, IN A LAND CALLED HONAH LEE.
"""

def read_message():
    """create the string and let the input string from user be stored in that string
    make a while loop to continue running, only break if input is blank twice"""
    message_list = []
    while True:
        input_message = input()
        if input_message == "":
            break
        message_list.append(input_message)
    return message_list

def main():
    print("Enter text rows to the message. Quit by entering an empty row.")
    message = read_message()
    print(f"The same, shouting:")
    for lines in message:
        complete_message = lines.upper()
        print(complete_message)

if __name__ == "__main__":
    main()
