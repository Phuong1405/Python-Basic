import csv

def read_file(filename):

        file = open(filename, "r")
        contact_read=file.read()

        something=contact_read.split(";")
        print(something)

        contact_dict={ }
"""
        for lines in something:
            contact_dict[lines[0]]= {"name":lines[1],"phone":lines[2],"email":lines[3], "skype":lines[4]}
            print(contact_read)
"""

        fee = open("contacts.csv", "r")
        reader = csv.reader(fee)
        contact_csv = { }

file = open(filename, "r")
contact_read = file.readline()
for line in file:
        dict(line)

something = contact_read.split(";")
print(something)

import csv

with open('contacts.csv', mode='r') as infile:
        reader = csv.reader(infile)
        mydict = {rows[0]: rows[1] for rows in reader}




#key;name;phone;email;skype


def main():
    read_file("contacts.csv")


if name == "main":
        main()