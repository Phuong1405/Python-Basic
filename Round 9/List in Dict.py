def main():
    alphabetical_index = {}
    while True:
        line = input("Enter the topic and the page number (end by an empty row):")
        if line == "":
            break

        data_fields = line.split()
        keyword = data_fields[0]
        page_number = int(data_fields[1])

        if keyword not in alphabetical_index:
            alphabetical_index[keyword] = []

        alphabetical_index[keyword].append(page_number)

    print(alphabetical_index)

    for keyword in sorted(alphabetical_index):
        print(keyword, "", end="")
        for nr in sorted(alphabetical_index[keyword]):
            print(nr, "", end="")
        print()

if __name__ == "__main__":
    main()