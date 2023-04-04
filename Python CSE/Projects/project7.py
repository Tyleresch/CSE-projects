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
    ''' Docstring'''
    cities = input("Enter cities names: ").split(",")
    files = []
    file_ptrs = []
    for city in cities:
        try:
            file_ptr = open(city + ".csv", "r", encoding = "utf-8")
            files.append(city)
            file_ptrs.append(file_ptr)
        except FileNotFoundError:
            print("\nError: File {} is not found")
    return files, file_ptrs

def read_files(cities_fp):
    ''' Docstring'''
    data = []
    for fp in cities_fp:
        reader = csv.reader(fp)
        next(reader) 
        next(reader) 
        rows = []
        for row_data in reader:
            for i in range(1, len(row_data)):
                row_data[i] = float(row_data[i]) if row_data[i] != '' else None
            rows.append(tuple(row_data))
        data.append(rows) 
    return data

def get_data_in_range(master_list, start_str, end_str):
    ''' Docstring'''
    filtered_data = []
    start_date_real = []
    end_date_real = []
    start_date_real = datetime.strptime(start_str, "%m/%d/%Y").date()
    end_date_real = datetime.strptime(end_str, "%m/%d/%Y").date()
    result = []
    data_tuple = []
    for row in master_list:
        filtered_data = []
        for data_tuple in row:
            data_date = datetime.strptime(data_tuple[0], "%m/%d/%Y").date()
            if start_date_real <= data_date <= end_date_real:
                filtered_data.append(data_tuple)
        if filtered_data == filtered_data:
            result.append(filtered_data)

    return result

def get_min(col, data, cities): 
    ''' Docstring'''
    result = []
    min_list = []
    for num, city in enumerate(cities):
        data_set = data[num] 
        for item in data_set:
            if item[col] != None:
                min_list.append(item[col])
                min_num = min(min_list)
        tuple_list = (city, min_num)
        result.append(tuple_list)
        tuple_list = [] 
        min_list = []
    return result 

 

def get_max(col, data, cities): 
    ''' Docstring'''
    result = []
    max_list = []
    for num, city in enumerate(cities):
        data_set = data[num] 
        for item in data_set:
            if item[col] != None:
                max_list.append(item[col])
                max_num = max(max_list)
        tuple_list = (city, max_num)
        result.append(tuple_list)
        tuple_list = [] 
        max_list = []
    return result 

def get_average(col, data, cities): 
    ''' Docstring'''
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
            avg = round(total / count, 2)
        else:
            avg = []
        result.append((city, avg))
    return result

def mode_helper(column_1):
    ''' Docstring'''
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
    ''' Docstring'''
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
    ''' Docstring'''
    result = []
    for category in categories:
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
    ''' Docstring'''
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
        repeated_val_2 = repeated[count][1][0]
        print("\t{}: ".format(city))
        print("\tMin: {:.2f} Max: {:.2f} Avg: {:.2f}".format(min_num, max_num, avg_city))
        print("\tMost common repeated values ({:} occurrences): {:}\n".format(repeated_val, repeated_val_2))
        #print("\tNo modes.")
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
            category = input("\nEnter desired category: ").lower().split(',')
            answer = get_data_in_range(tuples, start, end)
            if category[0] in COLUMNS:
                col = COLUMNS.index(category[0])
                col_1 = COLUMNS.index(category[1])
                name = get_min(col, answer, cities)
                name = get_min(col_1, answer, cities)
                name_6 = get_max(col_1, answer, cities)
                name_6 = get_max(col, answer, cities)
                for name_2 in name:
                    print(name_2)
                    print("\n\t{}: ".format(category))
                    print("\tLowest Average: {:s} = {:.2f} Highest Average: {:s} = {:.2f}".format(name_2[0], name_2[1]))
            elif category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()
        elif num == 5:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ").lower()
            answer = get_data_in_range(tuples, start, end)
            col = COLUMNS.index(category)
            print("\n\t{}: ".format(category))
            if category in COLUMNS:
                display = display_statistics(col,answer, cities)
            elif category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()
            num = int(input(MENU))
        elif num == 4:
            start = input("\nEnter a starting date (in mm/dd/yyyy format): ")
            end = input("\nEnter an ending date (in mm/dd/yyyy format): ")
            category = input("\nEnter desired category: ").lower()
            answer = get_data_in_range(tuples, start, end)
            if category in COLUMNS:
                col = COLUMNS.index(category)
                name = get_modes(col, answer, cities)
                print("\n\t{}: ".format(category))
                for name_2 in name:
                    print("\tMost common repeated values for {:s} ({:d} occurrences): {:}\n".format(name_2[0], name_2[2], name_2[1][0]))
            elif category not in COLUMNS:
                print("\n\t{} category is not found.".format(category))
                category = input("\nEnter desired category: ").lower()
                continue
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
                                           
