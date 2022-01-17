"""
Format the program's printout so that in the first section,
the approximate value of the pi is printed to the specificity of zero decimals
(ie. as an integer) and, in the second section,
to the specificity of four decimals.
The program's printout should thus look like this:

    The approximate value of pi is 3 or, if we want to get specific, 3.1416      
        """

def main():
    PI = 3.14159265358979323846
    print("The approximate value of pi is", round(PI), "or, if we want to get specific,", "%.4f" % PI)



if __name__ == "__main__":
    main()
