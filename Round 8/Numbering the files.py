"""Vu Tu Phuong Nguyen
Programming 1"""
def main():
    file_name = input("Enter the name of the file: ")
    file = open(file_name, mode = "r")

    counter = 1
    for reader in file:
        counter +=1
        file_line = reader.rstrip()
        print(f"{counter-1} {file_line}")
    file.close()


if __name__ == "__main__":
    main()
