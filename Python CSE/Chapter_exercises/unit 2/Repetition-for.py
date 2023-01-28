num_str = int(input("Input an int: \n"))
daddy = 0
while num_str > 0:
    daddy += 1 
    print(daddy)
    if num_str - 1 == daddy:
        break
    
