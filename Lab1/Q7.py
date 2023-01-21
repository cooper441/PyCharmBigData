import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linspace

print("Question 7")
while True:

    try:
        print("Enter a number: ")
        number = input()
        if number == "Done":
            break

        number = int(number)

    except ValueError:
        print("Not a number, bad data")