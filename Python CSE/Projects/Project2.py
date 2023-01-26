###########################################################
#Project 2 
#Car pricing rental
#  Print and Input stuff for the  
#   While loop
#   Ask for customer Code 
#   Ask for the days rented and beginnig and end of odometer
#   Print the summary of car based on customer code 
#   This will include price, miles traveled and all previuos information
#   Ask user if theu wish to continue 
###########################################################



BANNER = "\nWelcome to Horizons car rentals. \
\n\nAt the prompts, please enter the following: \
\n\tCustomer's classification code (a character: BD, D, W) \
\n\tNumber of days the vehicle was rented (int)\
\n\tOdometer reading at the start of the rental period (int)\
\n\tOdometer reading at the end of the rental period (int)"

PROMPT = '''\nWould you like to continue (A/B)? '''

"\nCustomer code (BD, D, W): "
"\n\t*** Invalid customer code. Try again. ***"
"\nCustomer code (BD, D, W): "
"\nNumber of days: "
"\nOdometer reading at the start: "
"\nOdometer reading at the end:   "    
"\n\nCustomer summary:"
"\tclassification code:"
"\trental period (days):"
"\todometer reading at start:"
"\todometer reading at end:  "
"\tnumber of miles driven: "
"\tamount due: $"
"\nThank you for your loyalty."

import math
print(BANNER) #This prints the Banner above for the user

user = input(PROMPT) #This asks the user if they want to continue 
color = ('n')
x = ("0")
answer = float(0)
travel = float(0) #This is the total amount of miles added
tyler = int(0) #This is the amount of days rented
Odometer_s = int(0) #This is the starting of the odometer
Odometer_e = int(0) #This is the ending of the odometer
miles = float(0) 
while user == 'A':
    color = input('\nCustomer code (BD, D, W): ') #This code asks the user for customer code
    if color == "BD":
            tyler = int(input('\nNumber of days: ')) #This code asks number of days rented
            Odometer_s = int(input('\nOdometer reading at the start: ')) #This code asks the starting odometer reading
            Odometer_e = int(input('\nOdometer reading at the end:   '))#This code asks for the ending odometer reading
            print('\n\nCustomer summary:')
            print('\tclassification code:', color)
            print('\trental period (days):', tyler)
            print('\todometer reading at start:', Odometer_s)
            print('\todometer reading at end:  ', Odometer_e)
            travel = ((Odometer_e - Odometer_s)/10) #This equation shows how many miles traveled
            if travel > 0: #This code is the equation for customer code BD 
                print('\tnumber of miles driven: ', float((Odometer_e - Odometer_s)/10))
                print('\tamount due: $', float(math.floor((40 * tyler) + ((Odometer_e - Odometer_s) * .25))))
                user = input(PROMPT)
            if travel < 0: #This code makes it so that the numbers will not glitch out if it is over 1000000 value
                print('\tnumber of miles driven: ', float(((Odometer_e + 1000000) - Odometer_s)/10))
                print('\tamount due: $', float((40 * tyler) + ((((Odometer_e + 1000000)- Odometer_s)/10) * .25)))
                user = input(PROMPT)
    if color == 'D': #This is all that will happen if person selects D as their customer code
            tyler = int(input('\nNumber of days: '))
            Odometer_s = int(input('\nOdometer reading at the start: '))
            Odometer_e = int(input('\nOdometer reading at the end:   '))
            print('\n\nCustomer summary:')
            print('\tclassification code:', color)
            print('\trental period (days):', tyler)
            print('\todometer reading at start:', Odometer_s)
            print('\todometer reading at end:  ', Odometer_e)
            print('\tnumber of miles driven: ', float((Odometer_e - Odometer_s)/10))
            travel = ((Odometer_e - Odometer_s)/10)
            if travel > 100: #This will charge person more if they drive over 100 miles
                print('\tamount due: $', float((60 * tyler) + ((((((Odometer_e - Odometer_s)/10)) - (tyler * 100)) * .25))))
                user = input(PROMPT)
            if travel < 100: #This will charge the person no extra if drive under 100 miles
                print('\tamount due: $', float(math.floor((60 * tyler))))
                user = input(PROMPT)
    if color == 'W': #This is all that will happen if person selects W as their customer code
            tyler = int(input('\nNumber of days: '))
            Odometer_s = int(input('\nOdometer reading at the start: '))
            Odometer_e = int(input('\nOdometer reading at the end:   '))
            print('\n\nCustomer summary:')
            print('\tclassification code:', color)
            print('\trental period (days):', tyler)
            print('\todometer reading at start:', Odometer_s)
            print('\todometer reading at end:  ', Odometer_e)
            print('\tnumber of miles driven: ', float((Odometer_e - Odometer_s)/10))
            travel = ((Odometer_e - Odometer_s)/10)
            travel_weekly = travel/math.ceil(tyler/7)
            if travel_weekly < 900: #This is a certain equation for when miles traveled is less than 900
                if tyler < 7: #This for when the person travels less than 7 days
                    print('\tamount due: $', float(math.floor((190 * (tyler/tyler)))))
                    user = input(PROMPT)  
                if tyler > 7: #This is for when the person travels more than 7 days 
                    print('\tamount due: $', float(math.floor((190 * (tyler/7)))))
                    user = input(PROMPT)
            if 900 < travel_weekly < 1500: #This is a certain equation for when the miles traveled is between 900 to 1500
                print('\tamount due: $', float(math.floor(((100 + 190) * math.ceil(tyler/7)))))
                user = input(PROMPT) 
            if travel_weekly > 1500: #This is a certain equation for what happens over 1500 miles
                answer = float((190 * math.ceil(tyler/7)) + 200 * math.ceil(tyler/7) + ((((Odometer_e - Odometer_s)/10) - (1500 * math.ceil(tyler/7))) *0.25))
                print('\tamount due: $', round(answer, 1))
                user = input(PROMPT)
    if color != 'BD' and color != 'D' and color != 'W': #If the inputted by the user does not equal any of the following an error will occur
            print('\n\t*** Invalid customer code. Try again. ***')
            
            continue #This makes it so the loop repeats itself
                   
            
if user != 'A': #If the person does not input A than the loop will end
    print('\nThank you for your loyalty.') 

