''' Insert heading comments here.'''


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
    bit = ''
    Quotient = 0
    while N != 0:
        Quotient = N // B 
        Remainder = N % B
        N = Quotient
        Remainder = str(Remainder)
        bit = Remainder + bit
    if len(bit) % 8 == 0: 
        return (bit)
    else:
        while len(bit) % 8 != 0:
            bit = str('0') + bit 
        return (bit)



    pass  # insert your code here

def basetonum( S, B ):
    '''Insert docstring here.'''
    Total_number = int(0)
    nums = len(S) - 1
    for i in range(len(S)):
        Total_number += int(S[i]) * B ** nums
        nums = nums -1 
    return(Total_number)


        
    pass  # insert your code here

def basetobase(B1,B2,s_in_B1):
    '''Insert docstring here.'''
    B1 = int(B1)
    B2 = int(B2)
    nums_1 = basetonum(s_in_B1, B1)
    return(numtobase(nums_1, B2))
    pass  # insert your code here

 
def encode_image(image,text,N):
    '''Insert docstring here.'''
    N = int(N)
    message = ''
    count = N - 1
    if image == '' or text == '':
        return(image)
    for i in text:
        message += numtobase(ord(i), 2) 
    
    message_place = 0 
    encoded_image = ''
    test = 1
    index = 0
    for i, ch in enumerate(image):
        index += 1
        if test == N: 
            if ch != message[message_place]:
                encoded_image += message[message_place]
            else:
                encoded_image += ch
            message_place += 1
            test = 1 

            if message_place >= len(message):
                break 
        else:
            encoded_image += ch 
            test += 1
    index = index -1
    # # print(type(i))
    # print(index)
    new_image = image[index:]
    # print(new_image)
    return(encoded_image + new_image[1:] )


    pass  # insert your code here


def decode_image(stego, N):
    
    message_bits = ''
    message = stego[N-1::N]
    message_nums = len(message)//8*8
    message = message[:message_nums] 
    ans = ''
    for i in range(0, len(message), 8):
        ans += chr(basetonum(message[i:i+8],2))
    
    return ans

    pass



def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    print(MENU)
    option = ''
    while option != 'X' or option == 'x':    
        option = input('\n\tEnter option: ')
        if option == 'A' or option == 'a':
            N = input("\n\tEnter N: ")
            while '.' in N or '-' in N:
                print("\n\tError: {} was not a valid non-negative integer.". format(N))
                N = input("\n\tEnter N: ")
            B = int(input("\n\tEnter Base: "))     
            while not (int(B) >= 2 and int(B) <= 10):
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
            while not (int(B) >= 2 and int(B) <= 10):
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B))
                B = input("\n\tEnter Base: ")
            S = str(S)
            B = int(B)
            print("\n\t {} in base {}: {}".format(S, B, basetonum( S, B )))
            continue
        elif option == 'C' or option == 'c':
            B1 = input("\n\tEnter base B1: ")
            B1 = int(B1)
            while not (int(B1) >= 2 and int(B1) <= 10):
                print("\n\tError: {} was not a valid integer between 2 and 10 inclusive.".format(B1))
                B1 = input("\n\tEnter base B1: ")
            B2 = input("\n\tEnter base B2: ")
            B2 = int(B2)
            while not (int(B2) >= 2 and int(B2) <= 10):
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
            while len(image) // int(N) >= len(text):
                print("\n\tImage not big enough to hold all the text to steganography")
                continue
            print("\n\t Original image: {}".format(image))
            print("\n\t Encoded image: {}".format(encode_image(image,text,N)))
            continue
        elif option == 'D' or option == 'd':

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
