###########################################################
#Project 7
#This project goes through many given files and sorts certain items that are wanted 
#It has 10 functions used to connect to the main 
#The main function is where everything for the UI of the progarm is printed 
#This progarm has a total of 7 options you can choose from
#Most functions with return a list of tuples 
###########################################################
import csv
from datetime import datetime
from operator import itemgetter

COLUMNS = ["date",  "average temp", "high temp", "low temp", "precipitation", \
           "snow", "snow depth"]

TOL = 0.02

BANNER = 'This program will take in csv files with weather data and compare \
the sets.\nThe data is available for high, low, and average temperatures,\
\nprecipitation, and snow and snow depth.'    


MENU = '''
        Menu Options:
        1. Highest value for a specific column for all cities
        2. Lowest value for a specific column for all cities
        3. Average value for a specific column for all cities
        4. Modes for a specific column for all cities
        5. Summary Statistics for a specific column for a specific city
        6. High and low averages for each category across all data
        7. Quit
        Menu Choice: '''
        
      
        
def open_files():
    '''Prompts the user to enter a comma-separated list of city names, and attempts to open a CSV file
    for each city using the `open` function. If a file is successfully opened, its corresponding city name
    and file pointer are added to separate lists. If a file is not found, an error message is printed to the console.
    '''
    # Prompt the user to enter a comma-separated list of city names
    cities = input("Enter cities names: ").split(",")

    # Create two empty lists to store the city names and file pointers
    files = []
    file_ptrs = []
    # Loop through each city in the list of cities
    for city in cities:
        try:
            # Try to open the corresponding CSV file for the current city
            file_ptr = open(city + ".csv", "r", encoding = "utf-8")
            files.append(city)
            file_ptrs.append(file_ptr)
        except FileNotFoundError:
            print("\nError: File {} is not found".format(city + '.csv'))
    # Return the lists of city names and file pointers
    return files, file_ptrs

def read_files(cities_fp):
    '''Reads CSV files using the `csv` module from a list of file pointers, and converts the data into
    a list of tuples. Assumes that the first two rows of each file are headers and skips them. Converts
    all numeric fields to float values, while keeping empty fields as None.
    '''
    data = []

    # Loop through each file pointer in the list of file pointers
    for fp in cities_fp:

        # Create a CSV reader object for the current file pointer
        reader = csv.reader(fp)
        # Skip the first two rows of the CSV file, which are assumed to be headers
        next(reader) 
        next(reader) 
        rows = []

        # Loop through each row of data in the CSV file
        for row_data in reader:
            for i in range(1, len(row_data)):
                row_data[i] = float(row_data[i]) if row_data[i] != '' else None
            # Convert the current row of data to a tuple and append it to the list of rows
            rows.append(tuple(row_data))
        # Append the list of rows to the list of data for all files
        data.append(rows) 
    # Return the list of data for all files
    return data

def get_data_in_range(master_list, start_str, end_str):
    '''ilters data from a master list of tuples by a given start and end date range, and returns a
    list of lists, where each inner list contains tuples representing rows of data that fall within
    the specified date range.
    '''
    filtered_data = []
    start_date_real = []
    end_date_real = []
    # Initialize variables to store the start and end dates as datetime.date objects
    start_date_real = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date_real = datetime.strptime(end_str, "%m/%d/%Y").date()
    result = []
    data_tuple = []
    # Loop through each row of data in the master list
    for row in master_list:
        filtered_data = []
        for data_tuple in row:
            # Convert the date string in the tuple to a datetime.date object
            data_date = datetime.strptime(data_tuple[0], "%m/%d/%Y").date()
            if start_date_real <= data_date <= end_date_real:
                filtered_data.append(data_tuple)
        # If the filtered data list is not empty, add it to the result list
        if filtered_data == filtered_data:
            result.append(filtered_data)

    return result

def get_min(col, data, cities): 
    '''Finds the minimum value in a given column for each city in a list of cities, based on data in a list
    of lists, and returns a list of tuples containing the city name and the corresponding minimum value.
    '''
    result = []
    min_list = []
    for num, city in enumerate(cities):
        # Get the data for the current city from the list of lists
        data_set = data[num] 
        # Loop through each row of data for the current city
        for item in data_set:
            if item[col] != None:
                min_list.append(item[col])
                # Find the minimum value in the list
                min_num = min(min_list)
        tuple_list = (city, min_num)
        result.append(tuple_list)
        tuple_list = [] 
        min_list = []
    return result 

 

def get_max(col, data, cities): 
    '''Finds the maximum value in a given column for each city in a list of cities, based on data in a list
    of lists, and returns a list of tuples containing the city name and the corresponding maximum value.
    '''
    result = []
    max_list = []
    # Loop through each row of data for the current city
    for num, city in enumerate(cities):
        data_set = data[num] 
        for item in data_set:
            if item[col] != None:
                max_list.append(item[col])
                # Find the max value in the list
                max_num = max(max_list)
        tuple_list = (city, max_num)
        result.append(tuple_list)
        tuple_list = [] 
        max_list = []
    return result 

def get_average(col, data, cities): 
    ''' This function takes a column index, a list of data sets, and a list of corresponding cities as input. It calculates the average value of the specified column for each city in the list of cities, rounded to two decimal places.
    '''
    result = []
    for num, city in enumerate(cities):
        data_set = data[num]
        total = 0
        count = 0
        for item in data_set:
            if item[col] != None:
                total += item[col]
                count += 1
        if count > 0:
            #Find the average value through math num divided by total
            avg = round(total / count, 2)
        else:
            avg = [] 
        result.append((city, avg))
    return result

def mode_helper(column_1):
    ''' The function mode_helper is a helper function that takes in a list of numbers as input and returns the mode(s) of the list along with their frequency.'''
    column_1.sort()
    n_1 = column_1[0]
    count = 1 
    L = []
    mode = []
    for num in column_1[1:]:
        if n_1 == 0:
            n_1 = num
            continue
        check = abs((n_1 - num)/ n_1)
        if check <= TOL:
            count += 1 
        else: 
            L.append((count, n_1))
            n_1 = num 
            count = 1
    L.append((count, n_1))
    result = max(L)
    result = result[0]
    if result != 1: 
        for tup in L:
            if tup[0] == result:
                mode.append(tup[1])
    return mode, result

#helped by andrew TA for get_modes and mode_helper

def get_modes(col, data, cities):
    ''' The function get_modes takes in a column index col, a list of data data, and a list of cities cities. It returns a list of tuples where each tuple contains the name of a city, its mode value(s), and the frequency of the mode value(s) in the corresponding column of data. If there are multiple mode values, they are returned as a list. If there is no mode value, an empty list is returned. The mode_helper function is used to calculate the mode(s) of a given column.'''
    result = []
    for i, city in enumerate(cities):
        column = []
        for item in data[i]:
            if item[col] != None:
                column.append(item[col])
        tup = mode_helper(column)
        result.append((city, tup[0], tup[1]))
    return result

          
def high_low_averages(data, cities, categories):
    '''Calculate the high, low, and average values for each category in each city, 
    and return a list of tuples containing the name of the city and the average value.
    '''
    result = []
    for category in categories:
        category = category.lower()
        if category not in COLUMNS:
            result.append(None)
            continue
        i = COLUMNS.index(category)
        new_list = []
        for city in cities:
            i_city = cities.index(city)
            
            values = [row[i] for row in data[i_city] if row[i] != None]

            if values:
                high = max(values)
                low = min(values)
                avg = sum(values) / len(values)
                new_list.append((city, round(avg, 2)))
        sorted_low = sorted(new_list, key = itemgetter(1))
        sorted_high = sorted(new_list, reverse = True, key = itemgetter(1))

        result.append([sorted_low[0], sorted_high[0]])
        
    return result

def display_statistics(col,data, cities):
    ''' The display_statistics function takes in a column index col, a list of data data, and a list of cities cities and displays statistics for each city related to the given column. It first calls the get_max, get_min, get_average, and get_modes helper functions to compute the maximum value, minimum value, average value, and most common repeated values for each city. It then prints out these statistics for each city in a user-friendly format.'''
    max_city = get_max(col, data, cities)
    min_city = get_min(col, data, cities)
    average_city = get_average(col, data, cities)
    repeated = get_modes(col, data, cities)
    count = 0
    count_1 = 1
    for city in cities:
        min_num = min_city[count][1]
        max_num = max_city[count][1]
        avg_city = average_city[count][1]
        repeated_val = repeated[count][2]
        print("\t{}: ".format(city))
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}".format(min_num, max_num, avg_city))
        try:
            repeated_val_2 = repeated[count][1][0]
        except:
            print("\tNo modes.")
            continue
        if repeated_val_2 != []: 
            print("\tMost common repeated values ({:} occurrences): {:}\n".format(repeated_val, repeated_val_2))
        elif repeated_val_2 == []:
            print("\tNo modes.")
        count +=1
        count_1 += 1

             
def main():
    print(BANNER)
    cities, file_opener = open_files()
    tuples = read_files(file_opener)
    num = int(input(MENU))
    if num not in [1,2,3,4,5,6,7]:
        num = MENU
    while num in [1,2,3,4,5,6,7]:
        if num == 7:
            print("\nThank you using this program!")
            break 
        elif num == 6:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            categories = input("\nEnter desired categories seperated by comma: ")
            answer = get_data_in_range(tuples, start, end)
            category1 = categories.split(",")
            data = high_low_averages(answer, cities, category1)
            print("\nHigh and low averages for each category across all data.")
            for categ in range(len(category1)):
                avg = data[categ]
                if avg:
                    print("\n\t{}: ".format(category1[categ].lower()))
                    print("\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}".format(avg[0][0], avg[0][1], avg[1][0], avg[1][1]))
                else:
                    print("\n\t{} category is not found.".format(category1[categ].lower()))
            num = int(input(MENU))
        elif num == 5:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ").lower()
            answer = get_data_in_range(tuples, start, end)
            while True:
                if category in COLUMNS:
                    print("\n\t{}: ".format(category))
                    col = COLUMNS.index(category)
                    display = display_statistics(col,answer, cities)
                    break
                elif category not in COLUMNS:
                    print("\n\t{} category is not found.".format(category))
                    category = input("\nEnter desired category: ").lower()
                    continue
            num = int(input(MENU))
        elif num == 4:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ").lower()
            answer = get_data_in_range(tuples, start, end)
            while True:
                if category in COLUMNS:
                    col = COLUMNS.index(category)
                    break
                else:
                    print("\n\t{} category is not found.".format(category))
                    category = input("\nEnter desired category: ").lower()
            name = get_modes(col, answer, cities)
            print("\n\t{}: ".format(category))
            for name_2 in name:
                print("\tMost common repeated values for {:s} ({:d} occurrences): {:}\n".format(name_2[0], name_2[2], name_2[1][0]))
            num = int(input(MENU))
        elif num == 3:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ").lower()
            answer = get_data_in_range(tuples, start, end)
            if category in COLUMNS:
                col = COLUMNS.index(category)
                name = get_average(col, answer, cities)
                print("\n\t{}: ".format(category))
                for name_2 in name:
                    print("\tAverage for {:s}: {:.2f}".format(name_2[0], name_2[1]))
            elif category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()
            num = int(input(MENU))
        elif num == 2:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ").lower()
            answer = get_data_in_range(tuples, start, end)
            if category in COLUMNS:
                col = COLUMNS.index(category)
                name = get_min(col, answer, cities)
                print("\n\t{}: ".format(category))
                for name_2 in name:
                    print("\tMin for {:s}: {:.2f}".format(name_2[0], name_2[1]))
            elif category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()
            num = int(input(MENU))
        elif num == 1:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ").lower()
            answer = get_data_in_range(tuples, start, end)
            if category in COLUMNS:
                col = COLUMNS.index(category)
                name = get_max(col, answer, cities)
                print("\n\t{}: ".format(category))
                for name_2 in name:
                    print("\tMax for {:s}: {:.2f}".format(name_2[0], name_2[1]))
            elif category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()
            num = int(input(MENU))
            

#DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
#ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
                                           
