def main():
    day = int(input("Enter the number of days: "))
    repetition = 1
    sum = 0
    counting = 0
    while repetition <= day:
        length = float(input(f"Enter day {repetition} running length: "))
        sum += length
        repetition += 1
        mean = float((f"{sum / day:.2f}"))

        if day == (repetition - 1):
            if mean >= 3.00:
                print()
                print(f"You were persistent runner! With a mean of {mean:.2f} km.")
            if mean < 3.00:
                print()
                print(f"Your running mean of {mean:.2f} km was too low!")
        if length == 0:
            counting += 1
            if counting >= 3:
                print()
                print("You had too many consecutive lazy days!")
                break
        else:
            counting = 0

if __name__ == "__main__":
    main()
