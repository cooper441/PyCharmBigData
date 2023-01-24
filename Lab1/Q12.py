"""
Python variables are pointers. If we have two variable names pointing to the
same mutable object, then they are aliases meaning changing one will change the
other as well. For example
# >>> x = [2, 4, 8]
# >>> y = x #y is an alias of x
# >>> x.append(10)
# >>> print(y)
# [2, 4, 8, 10]
# >>> print(x is y)
True
Numbers, strings, and other simple types are immutable: you can’t change their
value - you can only change what values the variables point to.
"""

"""
12.Write a program that prompts the user for a list of numbers and prints out 
the maximum and minimum of the numbers at the end when the user enters 
’done’. Store the numbers the user enters in a list and use the max() and 
min() functions to compute the maximum and minimum numbers after the 
loop completes. Return the sorted list of numbers read in. Handle exceptions 
appropriately.
Enter a number:2
Enter a number:5
Enter a number:7
Enter a number:3
Enter a number:9
Enter a number:4
Maximum: 9.0
Minimum: 2.0
"""
listOfNumbers = []
while True:

    try:

        toAdd = (input("Enter a number: "))

        if toAdd == "Done":
            listOfNumbers.sort()
            print(listOfNumbers)
            print("Max number is: " + str(max(listOfNumbers)))
            print("Min number is: " + str(min(listOfNumbers)))
            break

        toAdd = int(toAdd)
        listOfNumbers.append(toAdd)



    except ValueError:
        print("Not a number, bad data")
