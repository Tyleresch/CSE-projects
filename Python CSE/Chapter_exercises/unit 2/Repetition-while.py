sum = 0
while True: 
    num_str = int(input("Input an int: \n"))
    if num_str == 10:
         print(sum)
         break 
    else:
        sum = num_str + sum
    