#Read in a number and write out whether it is a perfect square or not. Any number which can be expressed as the product of two whole equal numbers is classified as a perfect square.
#For example, 64 can be written as 8*8 hence 64 is a perfect square.
#In the starter code, we import the math module. The Square root of the number is calculated with  math.sqrt() method.
#In case of a large number, the root calculated in Python may not be a perfectly whole number, it might be some decimal different. So, for the purpose of this exercises, we will take the floor value to get the desired outputs even if the input is large.


import math
nums = int(input("Enter the Number: "))
roots = math.sqrt(nums)
if int(roots + .5) ** 2 == nums:
     print("\nnumber is a perfect square")
else:
    print('\nnumber is not a perfect square')
#USE the following strings in your print and input statements
"Enter the Number: "
"\nnumber is a perfect square"
"\nnumber is not a perfect square"
