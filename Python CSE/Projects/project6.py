###########################################################
#Project 6
#There are a total of 10 defined functions in this project
#The 1st function - open_file()
#   While true loop and uses a try and except to open the file and prompts user at begining
#The 2nd function - get_books_by_criterion()
#   
#The 3rd function - read_file(fp)
#   
#The 4th function - get_books_by_criterion(list_of_tuples, criterion, value)
#   
#The 5th function - get_books_by_criteria(list_of_tuples, category, rating, page_number)
#   
#The 6th function - get_books_by_keyword(list_of_tuples, keywords)
#   
#The 7th function - sort_authors(list_of_tuples, a_z)
#   
#The 8th function - recommend_books(list_of_tuples, keywords, category, rating, page_number,  a_z = True)
#   
#The 9th function - display_books(list_of_tuples)
#   
#The 10th function - get_option()
#   
#The 11th function - main()
#   This function is just for the while loop
###########################################################

import csv
from operator import itemgetter

TITLE = 1
CATEGORY = 3
YEAR = 5
RATING = 6
PAGES = 7

MENU = "\nWelcome to the Book Recommendation Engine\n\
        Choose one of below options:\n\
        1. Find a book with a title\n\
        2. Filter books by a certain criteria\n\
        3. Recommend a book \n\
        4. Quit the program\n\
        Enter option: "

CRITERIA_INPUT = "\nChoose the following criteria\n\
                 (3) Category\n\
                 (5) Year Published\n\
                 (6) Average Rating (or higher) \n\
                 (7) Page Number (within 50 pages) \n\
                 Enter criteria number: "

def open_file():
    """  Prompts the user to enter a file name and attempts to open the file in read-only mode with UTF-8 encoding. 
    If the file is found, the function returns the file pointer. 
    If the file is not found, the function displays an error message and prompts the user to try again."""
    while True:
        file_name = input("Enter file name: ")
        try:
            fp = open(file_name, 'r', encoding='utf-8')
            return fp
        except FileNotFoundError:
            print("\nError opening file. Please try again.")


def read_file(fp):
    """Reads a CSV file and returns a list of tuples containing information about books, skipping the first row of headers. The function converts certain columns from the file into specific data types, such as converting the rating column to a float and the number of pages column to an integer. If any errors occur while reading the file, the function skips over the problematic row and continues reading the rest of the file. The resulting list of tuples contains the ISBN-13, title, authors, categories, description, year, rating, number of pages, and number of ratings for each book."""
    data = []
    reader = csv.reader(fp)
    next(reader) # skip header

    for row in reader:
        try:
            isbn13 = row[0]
            title = row[2]
            authors = row[4]
            categories = row[5].lower().split(',')
            description = row[7]
            year = row[8]
            rating = float(row[9])
            num_pages = int(row[10])
            rating_count = int(row[11])

            book = (isbn13, title, authors, categories, description, year, rating, num_pages, rating_count)
            data.append(book)
        except:
            continue

    return data


def get_books_by_criterion(list_of_tuples, criterion, value):
    """This function takes a list of book data and filters it based on a given criterion and value, where the criterion can be TITLE, CATEGORY, YEAR, PAGES, or RATING and the value depends on the criterion. It returns a list of book data tuples that match the given criterion and value, or an empty list if no matches are found."""
    filtered_books = []
    for book in list_of_tuples:
        if criterion == TITLE:
            if value.lower() == book[TITLE].lower():
                return book

        elif criterion == CATEGORY and value in book[CATEGORY]:
            filtered_books.append(book)
        elif criterion == YEAR and value == str(book[YEAR]):
            filtered_books.append(book)
        elif criterion == PAGES and int(value) - 50 <= int(book[PAGES]) <= int(value) + 50:
            filtered_books.append(book)
        elif criterion == RATING and float(value) <= float(book[RATING]):
            filtered_books.append(book)
    return filtered_books

def get_books_by_criteria(list_of_tuples, category, rating, page_number):
    """This function selects books from a list of book data tuples that match the given criteria, where the criteria include the book category, rating, and maximum number of pages, and it returns a list of tuples containing information about the selected books; if no matches are found, an empty list is returned."""
    filtered_list = get_books_by_criterion(list_of_tuples, CATEGORY, category)
    filtered_list = get_books_by_criterion(filtered_list, RATING, rating)
    filtered_list = get_books_by_criterion(filtered_list, PAGES, page_number)

    return filtered_list


def get_books_by_keyword(list_of_tuples, keywords):
    """This function takes in a list of book tuples and a list of keywords as arguments. It filters the book list by returning only the books that contain any of the keywords in their title or author's name. The result is returned as a list of book tuples that match the given keywords. The function has a docstring that provides a brief explanation of what it does."""
    result = [book for book in list_of_tuples if any(keyword.lower() in book[4].lower() for keyword in keywords)]
    return result

def sort_authors(list_of_tuples, a_z = True):
    """This function sorts a list of book data tuples by author name in either ascending or descending order, depending on the value of the optional parameter a_z (True for ascending order, False for descending order), and it returns a sorted list of book data tuples sorted by author name accordingly."""
    if a_z == True:
        sorted_books = sorted(list_of_tuples, key=itemgetter(2))
    
    if a_z == False:
        sorted_books = sorted(list_of_tuples, key=itemgetter(2), reverse = True)

    return sorted_books


def recommend_books(list_of_tuples, keywords, category, rating, page_number,  a_z = True):
    """This function selects books from a list of book data tuples that match the given criteria, which include book keywords, category, rating, and maximum number of pages, sorts the selected books by author name in either ascending or descending order depending on the value of the optional parameter a_z (True for ascending order, False for descending order), and returns a list of tuples containing information about the recommended books that match the given criteria."""
    filtered_list = get_books_by_criteria(list_of_tuples, category, rating, page_number)
    filtered_list = get_books_by_keyword(filtered_list, keywords)
    sorted_list = sort_authors(filtered_list, a_z)
    return sorted_list


def display_books(list_of_tuples):
    """This function takes a list of tuples as input and prints formatted information about the books in the list. If the input list is empty, it prints a message saying that there is nothing to print. Otherwise, it prints a header row followed by one row for each book in the list. Each row displays information such as ISBN-13, title, authors, year, rating, number of pages, and number of ratings, formatted in a specific way using the `str.format()` method. If a book's title or author name is longer than 35 characters, it is truncated to fit the column width. If a book's rating cannot be converted to a float, it is not printed. The function does not return anything."""
    if list_of_tuples == []: 
        print("Nothing to print.")
    else:
        print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format('ISBN-13', 'Title', "Authors", "Year", "Rating", "Number Pages", "Number Ratings"))
        
        for row in list_of_tuples:
            if len(row[1]) <= 35 and len(row[2]) <= 35:
                isbn13 = str(row[0])
                title = row[1]
                authors = row[2]
                year = str(row[5])
                try:
                    rating = float(row[6])
                except ValueError:
                    pass
                num_pages = str(row[7])
                rating_count = str(row[8])
                print("{:15s} {:35s} {:35s} {:6s} {:<8.2f} {:<15s} {:<15s}".format(isbn13, title, authors, year, rating, num_pages, rating_count))

def get_option():
    """This function prompts the user to enter a numerical option from a given menu and returns the selected option if it is valid (i.e., 1, 2, 3, or 4), or None if the option is invalid. It also prints an error message if the selected option is invalid."""
    option = int(input(MENU))
    if option in [1,2,3,4]:
        return option 
    else: 
        print("\nInvalid option")
        return None

        
def main():
    """This function is the main entry point of the book recommendation system. It interacts with the user to take inputs for different criteria to recommend books. It calls various helper functions to retrieve, sort, and display the books based on the user's input. The function loops until the user selects the exit option."""
    file_opener = open_file()
    tuples = read_file(file_opener)
    num = get_option()
    if num not in [1,2,3,4]:
        num = get_option()
   # print(type(num))
    while num in [1,2,3,4]:
        if num == 4:
            break 
        if num == 3:
            #works fine but the recommend books does not work still 
            ture = True
            category = input("\nEnter the desired category: ")
            rating = input("\nEnter the desired rating: ")
            
            while True:
                try:
                    rating = float(rating)
                    break
                except ValueError:
                    print("\nInvalid input")
                    rating = input("\nEnter the desired rating: ")
                    

            page_number = input("\nEnter the desired page number: ")
            while True:
                try:
                    page_number = int(page_number)
                    break
                except ValueError:
                    print("\nInvalid input")
                    rating = input("\nEnter the desired page number: ")

            sorting = input("\nEnter 1 for A-Z sorting, and 2 for Z-A sorting: ")
            if sorting == '1':
                a_z = True 
            elif sorting != '1':
                a_z = False 

            keywords = input("\nEnter keywords (space separated): ")
            keywords = keywords.split()
            print("\nBook Details:")
            recommend = recommend_books(tuples, keywords, category, rating, page_number, a_z)
            display_books(recommend)
            num = get_option()
            continue 
        if num == 2:
            while True:
                criteria_num = input(CRITERIA_INPUT)
                try:
                    criteria_num = int(criteria_num)
                    if criteria_num not in [3, 5, 6, 7]:
                        print("\nInvalid input")
                        continue
                    break
                except ValueError:
                    print("\nInvalid input")
            
            Recommend = input("\nEnter value: ")
            if criteria_num == 3:
                Recommend = Recommend.lower()
                books = get_books_by_criterion(tuples, 3, Recommend)
                sorted_books = sort_authors(books)
                print("\nBook Details:")
                display_books(sorted_books[0:30])
            elif criteria_num == 5:
                Recommend = Recommend.lower()
                books = get_books_by_criterion(tuples, 5, Recommend)
                sorted_books = sort_authors(books)
                print("\nBook Details:")
                display_books(sorted_books[0:30])
            elif criteria_num == 6:
                while True:
                    try:
                        Recommend = float(Recommend)
                        break
                    except ValueError:
                        print("\nInvalid input")
                        Recommend = input("\nEnter value: ")
                books = get_books_by_criterion(tuples, 6, Recommend)
                sorted_books = sort_authors(books)
                print("\nBook Details:")
                display_books(sorted_books[0:30])
            elif criteria_num == 7:
                while True:
                    try:
                        Recommend = int(Recommend)
                        break
                    except ValueError:
                        print("\nInvalid input")
                        Recommend = input("\nEnter value: ")
                books = get_books_by_criterion(tuples, 7, Recommend)
                sorted_books = sort_authors(books)
                print("\nBook Details:")
                display_books(sorted_books[0:30])
            num = get_option()
            continue 
        if num == 1:
            book_name = input("\nInput a book title: ")
            tuples_names = get_books_by_criterion(tuples, TITLE, book_name)
            #print(tuples_names)
            print("\nBook Details:")
            display_books([tuples_names])
            num = get_option()
            continue
        


# DO NOT CHANGE THESE TWO LINES
# These two lines allow this program to be imported into other code
# such as our function_test code allowing other functions to be run
# and tested without 'main' running.  However, when this program is
# run alone, 'main' will execute.
if __name__ == "__main__":
    main()
