''' Insert heading comments here.'''


MENU = '''\nPlease choose one of the options below:
             A. Convert a decimal number to another base system         
             B. Convert decimal number from another base.
             C. Convert from one representation system to another.
             E. Encode an image with a text.
             D. Decode an image.
             M. Display the menu of options.
             X. Exit from the program.'''
    
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


def decode_image(sego,N):
    '''Insert docstring here.'''
    pass  # insert your code here         

def main():
    BANNER = '''
               A long time ago in a galaxy far, far away...   
              A terrible civil war burns throughout the galaxy.      
  ~~ Your mission: Tatooine planet is under attack from stormtroopers,
                   and there is only one line of defense remaining        
                   It is up to you to stop the invasion and save the planet~~
    '''

    print(BANNER)
    
    pass  # insert your code here

# These two lines allow this program to be imported into other code
# such as our function tests code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
#DO NOT CHANGE THESE 2 lines  
if __name__ == '__main__': 
    main()
#nice 
