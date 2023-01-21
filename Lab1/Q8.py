import numpy as np
import math
import matplotlib.pyplot as plt
from numpy import linspace

# Question 8
print("Question 8")

# %matplotlib inline

# print(math.pi)  # pi value
# x = np.random.randn(100, 100)
# y = np.mean(x, 0)
# plt.plot(y)
# plt.show()

x = linspace(-4, 4)  # make 100 points between 0 and 1.
y = x**3 - 4
plt.scatter(x, y)
plt.show()


# print(max("Hello world"))
# print(len("Hello world"))
# print(float(32))
# print(math.sqrt(2))
