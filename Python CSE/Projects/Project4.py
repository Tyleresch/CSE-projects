''' Insert heading comments here.'''
###########################################################
#Project 4 
# There are 4 defined fucntions in this project 
# The first is numtobase, This function accepts as input a non-negative integer
#N and a base B ; it  returns a string representing the number N in base B.
#The second is basetonum This function accepts as input a string S and a base B
#where S represents a number in base B where B is between 2 and 10 inclusive.
#It  then return an integer in base 10 representing the same number as S
# The third is basetobase the function returns a string representing the same
#number in base B2. S_B1 is always of length multiple of 8.
# The fourth encode_image This function takes a binary string imagerepresenting
#the image, text representing the message to be hidden in the image and N
#representing how many bits represent each pixel, and returns another binary
#string as output.
# Finally there is a main function that has the menu that combines everything
#together
###########################################################

MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''

import math 

def numtobase( N, B ):
    '''Insert docstring here.'''
    bit = '' #this is just declaring variable 
    Quotient = 0
    while N != 0: # Loop until N becomes zero.
        Quotient = N // B # Compute the integer quotient.
        Remainder = N % B
        N = Quotient
        Remainder = str(Remainder) # Convert the remainder to a string.
        bit = Remainder + bit # Prepend the remainder to the result.
    if len(bit) % 8 == 0: #make sure that bit is able to be a whole number devisable by 8
        return (bit) # If the length of the result is divisible by 8, return it as is.
    else:
        while len(bit) % 8 != 0: # If the length of the result is not divisible by 8, add leading zeros.
            bit = str('0') + bit 
        return (bit)



    pass  # insert your code here

def basetonum( S, B ):
    '''Insert docstring here.'''
    Total_number = int(0)
    nums = len(S) - 1 # initialize the exponent for base B to the highest power
    for i in range(len(S)): # loop through each digit in the number
        Total_number += int(S[i]) * B ** nums # add the value of the digit times B to the power of the exponent
        nums = nums -1 
    return(Total_number) # return the total decimal value


        
    pass  # insert your code here

def basetobase(B1,B2,s_in_B1):
    '''Insert docstring here.'''
    B1 = int(B1)
    B2 = int(B2)
    nums_1 = basetonum(s_in_B1, B1)
    return(numtobase(nums_1, B2)) #this code pretty much uses basetonum and numtobase to make the new base
    pass  # insert your code here

 
def encode_image(image,text,N):
    '''Insert docstring here.'''
    N = int(N)  # Convert N to an integer
    message = ''
    count = N - 1
    if image == '' or text == '': # If either image or text is empty, return the original image
        return(image)
    for i in text:
        message += numtobase(ord(i), 2) 
    
    message_place = 0 
    encoded_image = ''
    test = 1
    index = 0
    # Iterate over each bit in the original image
    for i, ch in enumerate(image):
        index += 1
        # If we've used N bits, either encode a character or copy the original bit
        if test == N: 
            if ch != message[message_place]: # If the original bit doesn't match the message bit, encode the message bit
                encoded_image += message[message_place]
            else: # Otherwise, copy the original bit
                encoded_image += ch
            message_place += 1 # Move on to the next character in the message
            test = 1 
            # If we've encoded the entire message, stop encoding
            if message_place >= len(message):
                break 
        else: # If we haven't used N bits yet, copy the original bit
            encoded_image += ch 
            test += 1
    index = index -1
    new_image = image[index:]
    # print(new_image)
    return(encoded_image + new_image[1:] )


    pass  # insert your code here


def decode_image(stego, N):
    
    message_bits = ''
    message = stego[N-1::N]
    message_nums = len(message)//8*8
    message = message[:message_nums] #slicing message with the length of message_nums makes sure this numnber good to be put in the range function
    ans = ''
    for i in range(0, len(message), 8):
        ans += chr(basetonum(message[i:i+8],2))
    
    return ans #this returning the decoded image 

    pass



def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER) #print that banner for an intro
    print(MENU)#this is outside the while loop 
    option = ''#this is for user input 
    while option != 'X' or option == 'x':    #make sure the loop is going at the right time
        option = input('\n\tEnter option: ')
        if option == 'A' or option == 'a':
            N = input("\n\tEnter N: ")
            while '.' in N or '-' in N: #this is making sure the number is not negative or a decimal
                print("\n\tError: {} was not a valid non-negative integer.". format(N))
                N = input("\n\tEnter N: ")
            B = int(input("\n\tEnter Base: "))     
            while not (int(B) >= 2 and int(B) <= 10):#make sure vaule is betweeen 2 and 10
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                B = input("\n\tEnter Base: ")
            else:
                N = int(N)
                B = int(B)
                print("\n\t {} in base {}: {}".format(N, B, numtobase( N, B )))
            continue
        elif option == 'B' or option == 'b':
            S = input("\n\tEnter string number S: ")
            B = int(input("\n\tEnter Base: "))     
            while not (int(B) >= 2 and int(B) <= 10):#make sure vaule is betweeen 2 and 10
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                B = input("\n\tEnter Base: ")
            S = str(S)
            B = int(B)
            print("\n\t {} in base {}: {}".format(S, B, basetonum( S, B )))
            continue #progarm continues to loop 
        elif option == 'C' or option == 'c':
            B1 = input("\n\tEnter base B1: ") #input for user
            B1 = int(B1) #make sure it is an int so the progarm can take it
            while not (int(B1) >= 2 and int(B1) <= 10):
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B1))
                B1 = input("\n\tEnter base B1: ")
            B2 = input("\n\tEnter base B2: ")
            B2 = int(B2)
            while not (int(B2) >= 2 and int(B2) <= 10):#make sure vaule is betweeen 2 and 10
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B2))
                B2 = input("\n\tEnter base B2: ")
            s_in_B1 = input("\n\tEnter string number: ")
            s_in_B1 = str(s_in_B1)
            print("\n\t {} in base {} is {} in base {}...".format(s_in_B1, B1, basetobase(B1,B2,s_in_B1), B2))

            continue
        elif option == 'E' or option == 'e':
            image = input("\n\tEnter a binary string of an image: ")
            N = input("\n\tEnter number of bits used for pixels: ")
            text = input("\n\tEnter a text to hide in the image: ")
            if not len(image) >= len(text) * 8:#make sure the option can fit 
                print("\n\tImage not big enough to hold all the text to steganography")
                continue
            print("\n\t Original image: {}".format(image))
            print("\n\t Encoded image: {}".format(encode_image(image,text,N)))
            continue
        elif option == 'D' or option == 'd':
            stego = input("\n\tEnter an encoded string of an image: ")
            N = input("\n\tEnter number of bits used for pixels: ")
            N = int(N)
            stego = str(stego)
            print("\n\t Original text: {}".format(decode_image(stego, N)))

            continue
        elif option == 'M' or option == 'm':
            print(MENU)
            continue #This code just returns you back to menu 
        elif option == "X" or option == 'x':
            print('\nMay the force be with you.')
            break #this code ends the progarm 
        else: 
            print('\nError:  unrecognized option [{}]'.format(option.capitalize()))  
            print(MENU)
        continue #This code just returns you back to menu 


    
    pass  # insert your code here

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()
