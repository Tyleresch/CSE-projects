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
    """Docstring"""
    while True:
        file_name = input("Enter file name: ")
        try:
            fp = open(file_name, 'r', encoding='utf-8')
            return fp
        except FileNotFoundError:
            print(f'Error: {file_name} not found. Please enter a valid file name.')


def read_file(fp):
    """Docstring"""
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
    """Docstring"""
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
    """Docstring"""
    filtered_list = get_books_by_criterion(list_of_tuples, CATEGORY, category)
    filtered_list = get_books_by_criterion(filtered_list, RATING, rating)
    filtered_list = get_books_by_criterion(filtered_list, PAGES, page_number)

    return filtered_list


def get_books_by_keyword(list_of_tuples, keywords):
    """Docstring"""
    result = [book for book in list_of_tuples if any(keyword.lower() in book[4].lower() for keyword in keywords)]
    return result

def sort_authors(list_of_tuples, a_z = True):
    """Docstring"""
    if a_z == True:
        sorted_books = sorted(list_of_tuples, key=itemgetter(2))
    
    if a_z == False:
        sorted_books = sorted(list_of_tuples, key=itemgetter(2), reverse = True)

    return sorted_books


def recommend_books(list_of_tuples, keywords, category, rating, page_number,  a_z = True):
    """Docstring"""
    filtered_list = get_books_by_criteria(list_of_tuples, category, rating, page_number)
    filtered_list = get_books_by_keyword(filtered_list, keywords)
    sorted_list = sort_authors(filtered_list, a_z)
    return sorted_list


def display_books(list_of_tuples):

    print("{:15s} {:35s} {:35s} {:6s} {:8s} {:15s} {:15s}".format('ISBN-13', 'Title', "Authors", "Year", "Rating", "Number Pages", "Number Ratings"))
    for row in list_of_tuples:
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
    """Docstring"""
    option = int(input(MENU))
    if option in [1,2,3,4]:
        return option 
    else: 
        print("\nInvalid option")
        return None

        
def main():
    file_opener = open_file()
    tuples = read_file(file_opener)
    num = get_option()
   # print(type(num))
    while num in [1,2,3,4]:
        if num == 4:
            break 
        if num == 3:
            num = get_option()
            continue 
        if num == 2:
            criteria_num = input(CRITERIA_INPUT)
            if criteria_num == '3':
                Recommend = input("\nEnter value: ")
                books = get_books_by_criterion(tuples, 3, Recommend)
                sorted_books = sort_authors(books)
                print("\nBook Details:")
                display_books(sorted_books[0:30])
            elif criteria_num == '5':
                Recommend = input("\nEnter value: ")
                books = get_books_by_criterion(tuples, 5, Recommend)
                sorted_books = sort_authors(books)
                print("\nBook Details:")
                display_books(sorted_books[0:30])
            elif criteria_num == '6':
                Recommend = input("\nEnter value: ")
                books = get_books_by_criterion(tuples, 6, Recommend)
                sorted_books = sort_authors(books)
                print("\nBook Details:")
                display_books(sorted_books[0:30])
            elif criteria_num == '7':
                Recommend = input("\nEnter value:")
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
