"""
A program for managing a small phone book.
 message_list = []
    while True:
        input_message = input()
        if input_message == "":
            break
        message_list.append(input_message)
    return message_list




Implement a word density calculator that reads a piece of text from the user
and then prints how many times each of the words appears in the text, as in this example run:

EnteEnter rows of text for word counting. Empty row to quit.
I'm on a high way to hell
I'm on a high way to hell
It's going really well
Well it's only hell


a : 2 times
going : 1 times
hell : 3 times
high : 2 times
i'm : 2 times
it's : 2 times
on : 2 times
only : 1 times
really : 1 times
to : 2 times
way : 2 times
well : 2 times
The words in the list are printed in alphabetic order and all the letters are in lower-case.
A string separated from other strings with empty characters is considered a word
(separated from the text using a split method).

Programming tips:

You don't need to save the whole text entered by the user. It is enough that you go through every word entered by
the user and use a suitable data structure to count the occurences of every word showing up.
The data structure in question contains statistics of how the words show up. You need to save information on the word "hell" showing up three times and the word "really" one time.
When the information on the statistics is processed (a new word is added or the number of times a word shows up is increased), the user always knows what word is in question.
Thus, you should save the statistics to dict, where the key is the word in question.
In addition to word, save the information on how many times it shows up. This is the value contained by the dict.
The operation in can be used to check if the word is in dict, ie. whether it has shown up in the text earlier.
If not, add a new word to dict. What is the number of the times the word shows up?
Every time it shows up after this, the value in dict increases by one.
After the entire text has been reviewed, information has been saved on dict on what words were in the text,
as well as how many times they have shown up. Now you can print the information in the format presented by the task from the dict.

"""

def main():
    print("Enter rows of text for word counting. Empty row to quit.")
    all_list = dict()
    lines = []
    while True:
        message_line = input()
        if message_line == "":
            break
        lines.append(message_line)

    for line in lines:
        line = line.strip()
        line = line.lower()
        words = line.split(" ")
        for word in words:
            if word in all_list:
                all_list[word] += 1
            else:
                all_list[word] = 1
    keylist = all_list.keys()
    complete_key=sorted(keylist)
    for key in list(complete_key):
        print(key, ":", all_list[key], "times")


if __name__ == "__main__":
    main()
