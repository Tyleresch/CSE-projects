import math

x1_str = input("Input x1: \n")  # do not change this line
y1_str = input("Input y1: \n")  # do not change this line
x2_str = input("Input x2: \n")  # do not change this line
y2_str = input("Input y2: \n")  # do not change this line

# convert strings to ints
x1_str = int(x1_str)
y1_str = int(y1_str) 
x2_str = int(x2_str)
y2_str = int(y2_str)
d = ((y2_str - y1_str )** 2 + (x2_str - x1_str )** 2) ** 0.5

print("d =",d)  # do not change this line

