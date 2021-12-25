def main():
    value = int(input("How do you feel? (1-10) "))


    if 1 <= value <= 10:
     if value >= 4 and value <= 7:
        print("A suitable smiley would be :-|")
     elif 7 < value < 10:
        print("A suitable smiley would be :-)")
     elif 1 < value < 4:
        print("A suitable smiley would be :-(")
     elif value == 1:
        print("A suitable smiley would be :'(")
     elif value == 10:
        print("A suitable smiley would be :-D")

    else:
        print("Bad input!")



if __name__ == '__main__':
    main()