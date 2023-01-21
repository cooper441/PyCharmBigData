l1 = [1, 9, 7, 3, 5]
print(l1)
l2 = [e for e in range(10) if e % 2 == 1]
print(l2)
print(l1 == l2)
l3 = sorted(l1)
print(l3)
print(l2, l3)
print(l2 == l3)  # values testing have the same values in the same index
print(l2 is l3)  # testing same object = false
print(l2 is l2)  # l2 is the same object as l2 = True
