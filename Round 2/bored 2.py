"""
        The program you implemented in the previous section will not work properly when
        the user enters something other than "y", "Y", "n", or "N".
        Now, implement a whole new program, which only contains a repeating structure that asks the user's answer again
        if the answer is not "y", "Y", "n" or "N".
Examples of how the program operates:

Answer Y or N: q
Incorrect entry.
Answer Y or N: w
Incorrect entry.
Answer Y or N: n
You answered n
Answer Y or N: Y
You answered Y
Answer Y or N: N
You answered N
        """
def main():
        answer = input("Answer Y or N: ")
        while answer != "n" and answer != "N" and answer != "y" and answer != "Y":
                print("Incorrect entry.")
                answer = input("Answer Y or N: ")

        print("You answered", answer)

if __name__ == "__main__":
        main()