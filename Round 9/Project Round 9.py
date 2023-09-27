def main():
    network = {}
    filename = "friendships1.txt"
    file = open(filename, mode="r")

    for line in file:
        line = line.rstrip()

        # Any line in the input file which begins with # is
        # considered a comment line and is skipped.  You can
        # therefore add # characters in the beginning of the
        # lines to temporarily ignore some lines for testing
        # purposes.
        if len(line) > 0 and line[0] == "#":
            continue

        fields = line.split(";")

        # print(fields)
        for name in fields:
            if not name.isalpha():
                print(f"Fatal Error: '{name}' is not a valid name.")
                print(f"{name}------------------------------------")
                return None

        # "who" is the first name in the list eg.Helen in ['Helen', 'Greta', 'Florian', 'Irina']
        who = fields[0]
        for friend in fields[1:]:  # [0,'Greta', 'Florian', 'Irina']
            # Remember: add_friendship automatically records the
            # friendships in two ways: <friend> will be <who>'s friend,
            # and <who> will be <friend>'s friend.
            # print(f"{network},who: {who},whos friend: {friend}")
            network[who] = friend

        for i in sorted(network):
            print(i)
            for a in sorted(network[i]):
                print(f"- {a}")




if __name__ == "__main__":
    main()

if name1, name2 in network:
    network[name1] = []
    network[name2] = []

else:
    network[name1] = name2
    network[name2] = name1