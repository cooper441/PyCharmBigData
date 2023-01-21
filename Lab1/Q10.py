# question 10
data = "     X-DSPAM-Confidence: 0.8475   "


print(data)
data = data.replace(" ", "")
data = data.split(":")
float_point = float(data[1])
print(type(float_point))
print(float_point)









