#hello 
###########################################################
#Project 3 
# Mortgage Calculator
#
#
#
#
#
#
#
###########################################################
NUMBER_OF_PAYMENTS = int(360)    # 30-year fixed rate mortgage, 30 years * 12 monthly payments
SEATTLE_PROPERTY_TAX_RATE = 0.0092
SAN_FRANCISCO_PROPERTY_TAX_RATE = 0.0074
AUSTIN_PROPERTY_TAX_RATE = 0.0181
EAST_LANSING_PROPERTY_TAX_RATE = 0.0162
AVERAGE_NATIONAL_PROPERTY_TAX_RATE = 0.011
SEATTLE_PRICE_PER_SQ_FOOT = 499.0
SAN_FRANCISCO_PRICE_PER_SQ_FOOT = 1000.0
AUSTIN_PRICE_PER_SQ_FOOT = 349.0
EAST_LANSING_PRICE_PER_SQ_FOOT = 170.0
AVERAGE_NATIONAL_PRICE_PER_SQ_FOOT = 244.0
APR_2023 = 0.0668

#''' WRITE YOUR CODE USING THE CONSTANT VALUES ABOVE '''
print("\nMORTGAGE PLANNING CALCULATOR\n============================ ")
print("\nEnter a value for each of the following items or type 'NA' if unknown ")

location = input("\nWhere is the house you are considering (Seattle, San Francisco, Austin, East Lansing)? ")
square_feet = float()
pay = float(0)
is_he_poor_or_rich = float(0)
annual_percentage_rate = float(0)
yes_no = str('Y')
graph = " "
APR = float(0)
sq_feet_cost = float(0)
rate_interest = float(0)
real_apr = float(0)
price_of_square_feet_in_certain_location = float(0)
total_cost = float(0)
tax = float(0)
mortgage_payment = float(0)
Total_monthly = float(0)
new_rate_interest = float(0)
cost = float(0)
the_price_miuns_down_payment = float(0)
while yes_no == str('Y'):
   if location == 'East Lansing': 
        price_of_square_feet_in_certain_location = float(EAST_LANSING_PRICE_PER_SQ_FOOT)
        EAST_LANSING_PROPERTY_TAX_RATE = float(EAST_LANSING_PROPERTY_TAX_RATE)

        square_feet = input("\nWhat is the maximum square footage you are considering? ")

        if str(square_feet) == "NA" or str(square_feet) == 'N':
            square_feet = 2062
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        elif float(square_feet) > 0: 
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        if str(pay) == 'NA':
            pay = 40000 
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        elif float(pay) > 0: 
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        if str(is_he_poor_or_rich) == 'NA':
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
        elif float(is_he_poor_or_rich) > 0:
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
            if str(annual_percentage_rate) == "NA":
                if int(square_feet) == 2062:
                    #APR = float(APR_2023) 
                    rate_interest = (APR_2023/12)
                    pay = float(pay)
                    is_he_poor_or_rich = float(is_he_poor_or_rich)
                    prinple = pay / (((rate_interest*(1+rate_interest)**NUMBER_OF_PAYMENTS))/((1+rate_interest)**360 - 1)) + is_he_poor_or_rich
                    sq_feet_cost = prinple/ price_of_square_feet_in_certain_location
                    real_apr = rate_interest * 1200
                    print("\nIn {}, a maximum monthly payment of ${:.2f} allows the purchase of a house of {:.0f} sq. feet for ${:.0f}\n\t assuming a 30-year fixed rate mortgage with a ${:.0f} down payment at {:.1f}% APR." .format(location,pay, sq_feet_cost,prinple, is_he_poor_or_rich, real_apr))
                    yes_no = input('\nWould you like to make another attempt (Y or N)? ')
            elif annual_percentage_rate != 'NA':
                    APR = float(annual_percentage_rate)
                    rate_interest = (APR/12) 
                    pay = float(pay)
                    new_rate_interest = APR/1200
                    cost = float(square_feet) * float(price_of_square_feet_in_certain_location)
                    the_price_miuns_down_payment = cost - is_he_poor_or_rich
                    mortgage_payment = float(cost)*(float(new_rate_interest)*(1+float(new_rate_interest))**360/((1+float(new_rate_interest))**360 - 1))
                    is_he_poor_or_rich = float(is_he_poor_or_rich)
                    prinple = pay / (((new_rate_interest*(1+new_rate_interest)**NUMBER_OF_PAYMENTS))/((1+new_rate_interest)**360 - 1)) + is_he_poor_or_rich
                    real_apr = rate_interest * 12
                    total_cost = float(square_feet) * float(EAST_LANSING_PRICE_PER_SQ_FOOT)
                    tax = (total_cost * EAST_LANSING_PROPERTY_TAX_RATE) / 12
                    Total_monthly = tax + mortgage_payment
                    print("\nIn {}, an average {:.0f} sq. foot house would cost ${:.0f}.\nA 30-year fixed rate mortgage with a down payment of ${:.0f} at {:.1f}% APR results\n\tin an expected monthly payment of ${:.2f} (taxes) + ${:.0f} (mortgage payment) = ${:.0f}\n" .format(location, float(square_feet), float(total_cost) , float(pay), float(real_apr), tax, mortgage_payment, Total_monthly))
                    graph = input('Would you like to print the monthly payment schedule (Y or N)? ')
                    if graph == 'Y':
                        print('Yes')
                        #for number in range (0,NUMBER_OF_PAYMENTS +1)

                    yes_no = input('\nWould you like to make another attempt (Y or N)? ')
                    
            
   elif location == "Austin":
        price_of_square_feet_in_certain_location = AUSTIN_PRICE_PER_SQ_FOOT
        AUSTIN_PROPERTY_TAX_RATE = float(AUSTIN_PROPERTY_TAX_RATE)
        square_feet = input("\nWhat is the maximum square footage you are considering? ")
        if str(square_feet) == "NA" or str(square_feet) == 'N':
            square_feet = 2062
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        elif int(square_feet) > 0: 
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        if str(pay) == 'NA':
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        elif int(pay) > 0: 
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        if str(is_he_poor_or_rich) == 'NA':
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
        elif int(is_he_poor_or_rich) > 0:
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
            if str(annual_percentage_rate) == "NA":
                if int(square_feet) == 2062:
                    APR = float(APR_2023) * 100
                    rate_interest = APR/12
                    APR = round(APR, 1)
                    pay = int(pay)
                    square_feet = (((float(pay)/((float(rate_interest) * (1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS))/(((1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS)) -1))) + float(is_he_poor_or_rich)) / float(price_of_square_feet_in_certain_location))
                    sq_feet_cost = square_feet * price_of_square_feet_in_certain_location
                    print("\nIn {}, a maximum monthly payment of ${} allows the purchase of a house of {} sq. feet for ${:06.2f}\n\t assuming a 30-year fixed rate mortgage with a ${} down payment at {}% APR." .format(location,pay, square_feet,sq_feet_cost, is_he_poor_or_rich, APR))
                    yes_no = input('\nWould you like to make another attempt (Y or N)? ')
            elif annual_percentage_rate != 'NA':
                APR = float(annual_percentage_rate)
                rate_interest = float(APR)/12
                pay = float(pay)
                square_feet = (((float(pay)/((float(rate_interest) * (1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS))/(((1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS)) -1))) + float(is_he_poor_or_rich)) / float(price_of_square_feet_in_certain_location))
                print("\nIn {}, a maximum monthly payment of $1200.00 allows the purchase of a house of {} sq. feet for $211349\n\t assuming a 30-year fixed rate mortgage with a ${}down payment at {}% APR." .format(location, square_feet, is_he_poor_or_rich, APR))
                print('\nIn {}, an average {} sq. foot house would cost $170000.\nA 30-year fixed rate mortgage with a down payment of $ {} at {}% APR results\n\tin an expected monthly payment of $229.50 (taxes) + $565.77 (mortgage payment) = $795.27'.format(location, square_feet, is_he_poor_or_rich, annual_percentage_rate))
                
   elif location == "San Francisco":
        price_of_square_feet_in_certain_location = SAN_FRANCISCO_PRICE_PER_SQ_FOOT
        SAN_FRANCISCO_PROPERTY_TAX_RATE = float(SAN_FRANCISCO_PROPERTY_TAX_RATE)
        square_feet = input("\nWhat is the maximum square footage you are considering? ")
        if str(square_feet) == "NA" or str(square_feet) == 'N':
            square_feet = 2062
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        elif int(square_feet) > 0: 
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        if str(pay) == 'NA':
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        elif int(pay) > 0: 
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        if str(is_he_poor_or_rich) == 'NA':
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
        elif int(is_he_poor_or_rich) > 0:
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
            if str(annual_percentage_rate) == "NA":
                if int(square_feet) == 2062:
                    APR = float(APR_2023) * 100
                    rate_interest = APR/12
                    APR = round(APR, 1)
                    pay = int(pay)
                    square_feet = (((float(pay)/((float(rate_interest) * (1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS))/(((1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS)) -1))) + float(is_he_poor_or_rich)) / float(price_of_square_feet_in_certain_location))
                    sq_feet_cost = square_feet * price_of_square_feet_in_certain_location
                    print("\nIn {}, a maximum monthly payment of ${} allows the purchase of a house of {} sq. feet for ${:06.2f}\n\t assuming a 30-year fixed rate mortgage with a ${} down payment at {}% APR." .format(location,pay, square_feet,sq_feet_cost, is_he_poor_or_rich, APR))
                    yes_no = input('\nWould you like to make another attempt (Y or N)? ')
            elif annual_percentage_rate != 'NA':
                APR = float(annual_percentage_rate)
                rate_interest = float(APR)/12
                pay = float(pay)
                square_feet = (((float(pay)/((float(rate_interest) * (1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS))/(((1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS)) -1))) + float(is_he_poor_or_rich)) / float(price_of_square_feet_in_certain_location))
                sq_feet_cost = square_feet * price_of_square_feet_in_certain_location
                print("\nIn {}, a maximum monthly payment of $1200.00 allows the purchase of a house of {} sq. feet for $211349\n\t assuming a 30-year fixed rate mortgage with a ${}down payment at {}% APR." .format(location, square_feet, is_he_poor_or_rich, APR))
                print('\nIn {}, an average {} sq. foot house would cost $170000.\nA 30-year fixed rate mortgage with a down payment of $ {} at {}% APR results\n\tin an expected monthly payment of $229.50 (taxes) + $565.77 (mortgage payment) = $795.27'.format(location, square_feet, is_he_poor_or_rich, annual_percentage_rate))
        
        graph = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
   elif location == "Seattle":
        price_of_square_feet_in_certain_location = SEATTLE_PRICE_PER_SQ_FOOT
        SEATTLE_PROPERTY_TAX_RATE = float(SEATTLE_PROPERTY_TAX_RATE)
        square_feet = input("\nWhat is the maximum square footage you are considering? ")
        if str(square_feet) == "NA" or str(square_feet) == 'N':
            square_feet = 2062
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        elif int(square_feet) > 0: 
            pay = input("\nWhat is the maximum monthly payment you can afford? ")
        if str(pay) == 'NA':
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        elif int(pay) > 0: 
            is_he_poor_or_rich = input("\nHow much money can you put down as a down payment? ")
        if str(is_he_poor_or_rich) == 'NA':
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
        elif int(is_he_poor_or_rich) > 0:
            annual_percentage_rate = input("\nWhat is the current annual percentage rate? \n")
            if str(annual_percentage_rate) == "NA":
                if int(square_feet) == 2062:
                    APR = float(APR_2023) * 100
                    rate_interest = APR/12
                    APR = round(APR, 1)
                    pay = int(pay)
                    square_feet = (((float(pay)/((float(rate_interest) * (1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS))/(((1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS)) -1))) + float(is_he_poor_or_rich)) / float(price_of_square_feet_in_certain_location))
                    sq_feet_cost = square_feet * price_of_square_feet_in_certain_location
                    print("\nIn {}, a maximum monthly payment of ${} allows the purchase of a house of {} sq. feet for ${:06.2f}\n\t assuming a 30-year fixed rate mortgage with a ${} down payment at {}% APR." .format(location,pay, square_feet,sq_feet_cost, is_he_poor_or_rich, APR))
                    yes_no = input('\nWould you like to make another attempt (Y or N)? ')
            elif annual_percentage_rate != 'NA':
                APR = float(annual_percentage_rate)
                rate_interest = float(APR)/12
                pay = float(pay)
                square_feet = (((float(pay)/((float(rate_interest) * (1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS))/(((1 + float(rate_interest)) ** float(NUMBER_OF_PAYMENTS)) -1))) + float(is_he_poor_or_rich)) / float(price_of_square_feet_in_certain_location))
                sq_feet_cost = square_feet * price_of_square_feet_in_certain_location
                print("\nIn {}, a maximum monthly payment of $1200.00 allows the purchase of a house of {} sq. feet for $211349\n\t assuming a 30-year fixed rate mortgage with a ${}down payment at {}% APR." .format(location, square_feet, is_he_poor_or_rich, APR))
                if int(square_feet) != 2062:
                        print('\nIn {}, an average {} sq. foot house would cost $170000.\nA 30-year fixed rate mortgage with a down payment of $ {} at {}% APR results\n\tin an expected monthly payment of $229.50 (taxes) + $565.77 (mortgage payment) = $795.27'.format(location, square_feet, is_he_poor_or_rich, annual_percentage_rate))
                        graph = input('\nWould you like to print the monthly payment schedule (Y or N)? ')
                        yes_no = input('\nWould you like to make another attempt (Y or N)? ')   
    