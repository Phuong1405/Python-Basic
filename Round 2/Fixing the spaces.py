""""
Create a program that asks the user's name and
then greets them with the text in the example run below.
We intend you to format the printout exactly as in the example printout,
ie. so that that the comma printed after the user's name is attached to the
name without the name and the comma being separated with a space.

An example of how the program operates:

Tell us your name: Teemu
Hey Teemu, the printout formatting is going well!
        """
def main():
    name = input("Tell us your name: ")
    print(f"Hey {name}, the printout formatting is going well!")

if __name__ == "__main__":
        main()
