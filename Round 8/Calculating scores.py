"""Vu Tu Phuong Nguyen
Programming 1"""


def main():
    file_name = input("Enter the name of the score file: ")
    file_save = open(file_name, mode="r")
    print("Contestant score: ")
    file_lines = file_save.readlines()
    dictionary = {}
    for line in file_lines:
        #line = line.rstrip()
        #key and value with split will make the separate list value
        key, value = line.split()

        if key in dictionary:
            dictionary[key] += int(value)
        else:
            dictionary[key] = int(value)

    for i in sorted(dictionary):
        print(i, dictionary[i])

    file_save.close()

if __name__ == "__main__":
    main()


