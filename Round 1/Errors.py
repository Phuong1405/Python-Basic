def main():
    age = int(input("Please, enter your age: "))

    if age < 24 and age > 17:
        print("Your ride will cost:", 1.47)
    elif age < 16 and age > 7:
        print("Your ride will cost:", 1.02)
    elif age < 7:
        print("Your ride will cost:", 0.00)
    else:
        print("Your ride will cost:", 2.04)


if __name__ == "__main__":
    main()