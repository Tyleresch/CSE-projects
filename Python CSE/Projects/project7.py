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
            file_name = city.strip() + ".csv"
            file_ptr = open(file_name, "r")
            files.append(file_name)
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
    
    pass   # remove this line

def display_statistics(col,data, cities):
    ''' Docstring'''

    pass   # remove this line
             
def main():
    print(BANNER)
    weather = input('Enter cities names: ')
    print(MENU)
    pass   # remove this line

#DO NOT CHANGE THE FOLLOWING TWO LINES OR ADD TO THEM
#ALL USER INTERACTIONS SHOULD BE IMPLEMENTED IN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
                                           
