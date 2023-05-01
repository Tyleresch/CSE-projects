#Write a program that takes an input n and uses a for loop to print only the first n positive multiples of three (note that a while loop is not allowed).  No error checking of the input is necessary.
#NOTE Starter Code uses this prompt


#DO NOT CHANGE OR DELETE
#USE THIS PROMPT                     
"Input an integer: \n"
n = int(input("Input an integer: \n"))
for i in range(1, n+1):
    print(3*i)
