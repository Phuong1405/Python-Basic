"""        elif command == "P":
            convert = list(english_spanish.items())
            convert.sort()
            english_spanish = dict(convert)

            for word in english_spanish:
                print(word, english_spanish[word])"""

"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Student Id:
Name: VU TU PHUONG NGUYEN
Email: phuong.nguyen@tuni.fi

Template for sorting by price assignment.
"""

PRICES = {
    "milk": 1.09, "fish": 4.56, "bread": 2.10,
    "chocolate": 2.70, "grasshopper": 13.25,
    "sushi": 19.90, "noodles": 0.97, "beans": 0.87,
    "bananas": 1.05, "Pepsi": 3.15,  "pizza": 4.15,
}


def main():

    convert_values = list(PRICES.values()) 
    sort_price = sorted(list(PRICES.values()))
    keys = list(PRICES.keys())

    for i in range(0, len(convert_values)):
        print(f"{keys[convert_values.index(sort_price[i])]} {sort_price[i]:.2f}")

if __name__ == "__main__":
    main()
