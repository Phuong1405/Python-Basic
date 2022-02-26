"""
COMP.CS.100 Programming 1
Project
This project was written by Johnson Apanishile and VU TU PHUONG NGUYEN

Mean (i.e. Average)
Variance
Standard Deviation
Using the Calculated Characteristic Values in This Project

In addition the program will print a histogram (i.e. a bar chart) which helps you to visualize how the values of the data set are located in the vicinity of the mean value.

The histogram is always expressed using six categories (bars). The bounds of the categories are calculated as follows (
σ
 as usual means the standard deviation of the data set):

0.0–0.5⋅σ
0.5⋅σ–1.0⋅σ
1.0⋅σ–1.5⋅σ
1.5⋅σ–2.0⋅σ
2.0⋅σ–2.5⋅σ
2.5⋅σ–3.0⋅σ

IIn the case of our earlier example, when the 
σ
 was calculated as 1.49 (or more accurately 1.48804761828568990378),
 the bounds of the categories will be:


category 0: 0.00–0.74
category 1: 0.74–1.49
category 2: 1.49–2.23
category 3: 2.23–2.98
category 4: 2.98–3.72
category 5: 3.72–4.46

You should note, that in your program code you can calculate the lower and upper bounds of the categories with a loop:

for category_number in range(0, 6):
    lower_bound = category_number * 0.5 * standard_deviation
    upper_bound = (category_number + 1) * 0.5 * standard_deviation

    # Here you place the code using the calculated values.
    # As an example, we'll just print the values on the screen.

    print(f"{category_number} {lower_bound:.2f}-{upper_bound:.2f}")
The decision of which category does a data set value belongs to is done as follows:

subtract the mean value from the data set value being processed and then
calculate the absolute value of the result.
Compare the result with the bounds of the six categories and select the matching one.

Again, continuing the familiar example where the mean was calculated as 3.25:


|5−3.25|=1.75 - Belongs to category 2
|4−3.25|=0.75 - Belongs to category 1
|2−3.25|=1.25 - Belongs to category 1
|3−3.25|=0.25 - Belongs to category 0
|1−3.25|=2.25 - Belongs to category 3
|4−3.25|=0.75 - Belongs to category 1 
|5−3.25|=1.75 - Belongs to category 2
|2−3.25|=1.25 - Belongs to category 1

You should note, even if the example didn't show it, that a value of the data set can differ from the mean so much that it does not belong to any category. In you program it means that the value in question is completely ignored when printing the histogram. There is a mathematical reason for this, but that is beyond the scope of this assignment.

One more note about the categories. If the calculation,
when trying the decide the category where a data value belongs,
gives a result which happens to be exactly on a boundary between two categories,
the data value is considered to belong to the higher category.
For example, if the absolute value of the difference between a data value and
the mean ended up being 2.23 in our example,
the data value would belong to the category 3.


Program Behavior
When the program starts it prints out the lines:

Enter the data, one value per line.
End by entering empty line.
Then the program starts reading inputs from the user and continues until the user enters an empty line. The values the user enter should be integers or floats.

If the user enters less than two numbers before the empty line, the program should print the error message:

Error: needs two or more values.
After this the program quits without further outputs.

Otherwise the program start processing the values the user entered and prints out their mean and standard deviation values:

The mean of given data was: X.XX
The standard deviation of given data was: Y.YY
Where X.XX is the mean value with two decimals ajd on annetun aineiston keskiarvo kahden Y.YY is the standard deviation with two decimals.

Näiden tilastollisten lukujen perään ohjelma tulostaa histogrammin ja lopettaa toimintansa:

After these two lines the program prints the histogram in the following format and when done, quits without forther output:

Values between std. dev. Z.ZZ-Z.ZZ: *************
Values between std. dev. Z.ZZ-Z.ZZ: **
Values between std. dev. Z.ZZ-Z.ZZ: ****
Values between std. dev. Z.ZZ-Z.ZZ: *
Values between std. dev. Z.ZZ-Z.ZZ: **
Values between std. dev. Z.ZZ-Z.ZZ: *
The Z.ZZ above are placeholders for the lower and upper bounds of the categories printed with two decimals. At the end of the each line the program prints as many * characters as there are data values belong to the category in question.

There is one exception: if the standard deviation of the data set is exactly 0, the program should print:

Deviation is zero.
and quit without printing the histogram.

Examples of Running the Program
Below you can study a few example runs of a program to help you understand how it should behave.

The Example Used Above
Enter the data, one value per line.
End by entering empty line.
5
4
2
3
1
4
5
2

The mean of given data was: 3.25
The standard deviation of given data was: 1.49
Values between std. dev. 0.00-0.74: *
Values between std. dev. 0.74-1.49: ****
Values between std. dev. 1.49-2.23: **
Values between std. dev. 2.23-2.98: *
Values between std. dev. 2.98-3.72:
Values between std. dev. 3.72-4.46:
A Small Data Set
Enter the data, one value per line.
End by entering empty line.
1
-1
0

The mean of given data was: 0.00
The standard deviation of given data was: 1.00
Values between std. dev. 0.00-0.50: *
Values between std. dev. 0.50-1.00:
Values between std. dev. 1.00-1.50: **
Values between std. dev. 1.50-2.00:
Values between std. dev. 2.00-2.50:
Values between std. dev. 2.50-3.00:
A Boring Data Set
Enter the data, one value per line.
End by entering empty line.
1
1
1
1
1

The mean of given data was: 1.00
The standard deviation of given data was: 0.00
Deviation is zero.
A Slightly Larger Data Set
Enter the data, one value per line.
End by entering empty line.
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
10.0

The mean of given data was: 5.50
The standard deviation of given data was: 3.03
Values between std. dev. 0.00-1.51: ****
Values between std. dev. 1.51-3.03: **
Values between std. dev. 3.03-4.54: ****
Values between std. dev. 4.54-6.06:
Values between std. dev. 6.06-7.57:
Values between std. dev. 7.57-9.08:

"""
"""
COMP.CS.100 Programming 1
Project
This project was written by Johnson Apanishile and VU TU PHUONG NGUYEN
"""
import math

def mean(data_list):
    """
    this function collects a data list
    and calculates and returns the mean
    :param data_list: float, list number user inputs
    return: float, the mean value
    """
    n= len(data_list)
    mean = sum(data_list)/n
    return mean

def variance(data_list):
    """
    this function collects a data list
    and calculates and returns the variance
    :param data_list: float, from the data list user inputs
    return: float, the value of variance
    """
    n= len(data_list)
    mean = sum(data_list) / n
    dev = [(x - mean) ** 2 for x in data_list]
    variance = sum(dev) / (n-1)
    return variance

def std(data_list):
    """
    this function collects a data list
    and calculates and returns the standard deviation
    using import sqrt
    :param data_list: float, from the data list user inputs
    return: float, the value of standard deviation
    """
    var = variance(data_list)
    std1 = math.sqrt(var)
    return std1

def graph(std, mean, data_list):
    """
    this function collects a data list, standard dev
    and data list as parameters
    and calculates and returns the variance
    :param std: float, standard deviation that calcualted in the function std
    :param mean: float,mean value that calculated in the function mean
    :param data_list:float, the list is taken from the user inputs
    """
    graph_list = []
    for x in data_list:
        #abs function is used here
        graph_val = float(abs(x - mean))
        graph_list.append(graph_val)


    for category_number in range(0, 6):
        lower_bound = category_number * 0.5 * std
        upper_bound = (category_number + 1) * 0.5 * std
        count = 0
        if lower_bound == 0 and upper_bound == 0:
            print("Deviation is zero.")
            break

        else:
            for i in graph_list:
                if lower_bound <= i < upper_bound:
                    count+= 1

            print(f"Values between std. dev. {lower_bound:.2f}-{upper_bound:.2f}: {'*' * count}")

def main():
    """
    Gets the user input and stores it in a list
    """

    print("Enter the data, one value per line.\nEnd by entering empty line.")
    #this collects the values and stores them in a list, breaks with an empty space
    #using try and except
    data_list = []
    while True:
        try:
            data = float(input())
        except ValueError:
            break
        data_list.append(data)
    if len(data_list) < 2:
        print("Error: needs two or more values.")
    else:
        #returns mean value
        print(f"The mean of given data was: {mean(data_list):.2f}")
        #returns standard deviation
        print(f"The standard deviation of given data was: {std(data_list):.2f}")
        #return the graph function with all the neccessary parameters
        graph(std(data_list),mean(data_list),data_list)


if __name__=="__main__":
    main()
