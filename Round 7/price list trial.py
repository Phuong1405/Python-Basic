"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name: Vu Tu Phuong Nguyen
Email: phuong.nguyen@tuni.fi

Template for pricelist assignment.

To clarify the examples color coding is used to represent the characters entered by the user, character "⏎" indicates the Enter key, and as usual, "␣" means whitespace.

The program ends when the user enters an empty line:

Enter product name:␣⏎
Bye!
Also, an inut line consisting only whitespace charactes is interpreted as an empty line:

Enter product name:␣␣␣␣␣⏎
Bye!
If the user enters a known product name (i.e. a name that is used as a key in the PRICES dictionary), the program prints its price as follows:

Enter product name:␣milk⏎
The price of milk is 1.09 e
Enter product name:␣
All prices are printed with two decimals.

If the product name is unknown, an error message will be printed:

Enter product name:␣pumpkin⏎
Error: pumpkin is unknown.
Enter product name:␣
When the used enters the product name, whitespaces in front of it and after it are ignored:

Enter product name:␣␣␣␣milk␣␣⏎
The price of milk is 1.09 e
Enter product name:␣
The same goes with errorneuos inputs: the extra whitespace characters will be ignored:

Enter product name:␣␣␣meat␣␣␣⏎
Error: meat is unknown.
Enter product name:␣
Hint: the removal of whitespaces might require you to peek string type's documentation.
"""
PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.7, "grasshopper": 13.25,
    "sushi": 19.9, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}

def main():
    product_name= input("Enter product name: ")
    goods = product_name.strip()

    while True:
            if goods not in PRICES and goods != "" and goods != " ":
                print(f"Error: {goods} is unknown.")
                product_name= input("Enter product name: ")
                goods = product_name.strip()

            elif goods in PRICES:
                x = PRICES[goods]
                print(f"The price of {goods} is {x:.2f} e")
                product_name = input("Enter product name: ")
                goods = product_name.strip()

            elif goods == " " or goods == "":
                print("Bye!")
                break

if __name__ == "__main__":
    main()
