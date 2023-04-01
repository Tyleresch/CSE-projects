#You are registering vehicles for the state of MI. Calculate and print the total fees.       Here are the details.

# All vehicles pay a $20.00 fee.

# If a vehicle has a special license plate, there is an additional $5.50 fee.

# An electric vehicle pays a $500.00 fee (to make up for not paying gas taxes)

# A moped pays $5.00

# An automobile pays $20.00

# Begin by asking if the user wants to register a vehicle.      Quit the program if the user answers anything except "yes".      If the user answers "yes" , you ask if the user has a special license plate and if it is a moped or automobile.

# The code then should print the total fee left justified with precision 2 and then ask if the user wants to register a vehicle.

# All responses can be upper or lower case letters or a mixture (case insensitive).

# No error checking is necessary on inputs for license plate, electric or vehicle type.      For example, when you ask for a vehicle you will only get one of the two possible responses: moped or automobile.

# The starter code will have all the strings that you need. If you do not see them, click on the Reset to Template button

# Input may be in any combination of upper and lower case letters. That is "Yes", "YES", "yEs", etc. all count as "yes".        Your code is expected to be able to handle all valid input, i.e. car, truck, yes, no, red, blue, white.

# Example 1 interaction:

# Do you want to register a vehicle (yes or no): yEs      Special license plate (yes or no): nO      Is your vehicle electric (yes or no): No      Is your vehicle a moped or automobile: mopeD      Your total fee is: $25.00      Do you want to register a vehicle (yes or no): Yes      Special license plate (yes or no): yeS      Is your vehicle electric (yes or no): Yes      Is your vehicle a moped or automobile: automoBile

# Your total fee is: $545.50      Do you want to register a vehicle (yes or no): No

# Example 2 interaction:

# Do you want to register a vehicle (yes or no): yes

# Special license plate (yes or no): yes

# Is your vehicle electric (yes or no): yes

# Is your vehicle a moped or automobile: automobile

# Your total fee is: $545.50

# Do you want to register a vehicle (yes or no): no



#USE THIS STRINGS IN YOUR INPUT AND PRINT STATEMENTS                    
"\nDo you want to register a vehicle (yes or no): "
"\nSpecial license plate (yes or no): "
"\nIs your vehicle electric (yes or no): "
""
"\nYour total fee is: ${}"
"\nDo you want to register a vehicle (yes or no): "
def main():
    fee = 20.00
    while True:
        yes_no = input('\nDo you want to register a vehicle (yes or no): ')
        if yes_no.lower() == 'yes':
            fee = 20
        elif yes_no.lower() != 'yes':
            print("")
            break
        speical = input('\nSpecial license plate (yes or no): ')
        if speical.lower() == 'yes':
            fee += 5.50 
        electric = input('\nIs your vehicle electric (yes or no): ')
        if electric.lower() == 'yes':
            fee+= 500.00
        vehicle =input('\nIs your vehicle a moped or automobile: ')
        if vehicle.lower() == 'moped':
            fee += 5.00
        elif vehicle.lower() == 'automobile':
            fee += 20.00
        print(f"\nYour total fee is: ${fee:.2f}")
        fee = 20.00




if __name__ =='__main__':
    main()
        

