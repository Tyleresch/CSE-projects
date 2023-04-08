import csv
from operator import itemgetter


MENU = '''\nSelect from the option: 
        1.Games in a certain year 
        2. Games by a Developer 
        3. Games of a Genre 
        4. Games by a developer in a year 
        5. Games of a Genre with no discount 
        6. Games by a developer with discount 
        7. Exit 
        Option: '''
        
      
        
def open_file(s):
    ''' Docstring '''
    while True:
        file_name = input(f'\nEnter {s} file: ')
        try:
            fp = open(file_name, "r", encoding="UTF-8")
            return fp
        except FileNotFoundError:
            print('\nNo Such file')
        except:
            print('\nNo Such file')

def read_file(fp_games):
    ''' Docstring'''
    readed = csv.reader(fp_games)
    next(fp_games)

    games_dict = {}

    for row in readed:
        name = row[0]
        date = row[1]
        developer = row[2].split(';')
        genres = row[3].split(';')
        first_mode = row[4].lower().split(';')
        mode = 0 if 'multi-player' == first_mode[0] else 1
        price = row[5].replace(',', '')
        try:
            price = float(price) * 0.012
        except ValueError:
            price = 0.0
        overall_reviews = row[6]
        reviews = int(row[7])
        percent_positive = int(row[8].replace('%', ''))
        support = []
        if row[9] == '1':
            support.append('win_support')
        if row[10] == '1':
            support.append('mac_support')
        if row[11] == '1':
            support.append('lin_support')
        

        games_dict[name] = [date, developer, genres, mode, price, overall_reviews, reviews, percent_positive, support]

    return games_dict
    #do 

def read_discount(fp_discount):
    ''' Docstring'''
    discount_dict = {}
    readed = csv.reader(fp_discount)
    next(readed)

    for line in readed:
        name = line[0] 
        discount = line[1]
        discount = float(discount)
        discount = round(discount, 2)
        discount_dict[name] = discount 

    return discount_dict

def in_year(master_D,year):
    ''' Docstring'''
    games = []
    for game, details in master_D.items():
        release_date = details[0]
        if int(release_date.split("/")[-1]) == year:
            games.append(game)
    return sorted(games)

def by_genre(master_D,genre): 
    ''' Docstring'''
    genre_games = {}
    for game, info in master_D.items():
        if genre in info[2]:
            genre_games[game] = info[7]
            sorted_games = sorted(genre_games.items(), key=lambda x: x[1], reverse=True)
    return [game[0] for game in sorted_games]

# def sort_key(game):
#     return (-game[1], game[2])
        
def by_dev(master_D,developer): 
    ''' Docstring'''
    dev_games = []
    for game, game_info in master_D.items():
        if developer in game_info[1]:
            dev_games.append((game, int(game_info[0].split('/')[-1])))
            dev_games.sort(key=lambda x: x[1], reverse=True)
    return [game[0] for game in dev_games]
    pass   # remove this line

def per_discount(master_D,games,discount_D): 
    ''' Docstring'''
    prices = []
    for game in games:
        if game in discount_D:
            price = master_D[game][4]
            discount_perc = discount_D[game]
            discounted_price = round((1 - discount_perc/100) * price, 6)
            prices.append(discounted_price)
        elif game not in discount_D:
            prices.append(master_D[game][4])
    return prices
    pass   # remove this line
    #do

def by_dev_year(master_D,discount_D,developer,year):
    ''' Docstring'''
    games = []
    for name, info in master_D.items():
        if developer in info[1] and int(info[0][-4:]) == year:
            if name in discount_D:
                price = round(info[4] * (100 - discount_D[name]) / 100, 2)
            else:
                price = info[4]
            games.append((name, price))
    games.sort(key=lambda x: x[1])
    return [name for name, _ in games]

    pass   # remove this line
    #do
          
def by_genre_no_disc(master_D,discount_D,genre):
    ''' Docstring'''
    genre_games = {}
    for game, info in master_D.items():
        if genre in info[2] and game not in discount_D:
            genre_games[game] = (info[4], info[7])
            sorted_games = sorted(genre_games.items(), key=lambda x: (x[1][0], -x[1][1]))
    return [game[0] for game in sorted_games]
    pass   # remove this line

def by_dev_with_disc(master_D,discount_D,developer):
    ''' Docstring'''
    dev_games = {}
    for game, info in master_D.items():
        if developer in info[1] and game in discount_D:
            dev_games[game] = (info[4], int(info[0].split('/')[2]))

    sorted_games = sorted(dev_games.items(), key=lambda x: (x[1][0], -x[1][1]))
    return [game[0] for game in sorted_games]
    pass   # remove this line
    
             
def main():
    fp_games = open_file("games")
    master_D = read_file(fp_games)
    fp_discount = open_file("discount")
    discount_D = read_discount(fp_discount)

    num = int(input(MENU))
    if num not in [1,2,3,4,5,6,7]:
        print("\nInvalid option")
        num = input(MENU)
    while num in [1, 2, 3, 4, 5, 6, 7]:
        if num == 1:
            year = int(input('\nWhich year: '))
            print("\nGames released in {}:".format(year))
            games = in_year(master_D, year)
            print(', '.join(games) if games else "Nothing to print")
        elif num == 2:
            developer = input('\nWhich developer: ')
            print("\nGames made by {}:".format(developer))
            games = by_dev(master_D, developer)
            print(', '.join(games) if games else "Nothing to print")
        elif num == 3:
            genre = input('\nWhich genre: ')
            print("\nGames with {} genre:".format(genre))
            games = by_genre(master_D, genre)
            print(', '.join(games) if games else "Nothing to print")
        elif num == 4:
            developer = input('\nWhich developer: ')
            year = int(input('\nWhich year: '))
            print("\nGames made by {} and released in {}:".format(developer, year))
            games = by_dev_year(master_D, discount_D, developer, year)
            print(', '.join(games) if games else "Nothing to print")
        elif num == 5:
            genre = input('\nWhich genre: ')
            print("\nGames with {} genre and without a discount:".format(genre))
            games = by_genre_no_disc(master_D, discount_D, genre)
            print(', '.join(games) if games else "Nothing to print")
        elif num == 6:
            developer = input('\nWhich developer: ')
            print("\nGames made by {} which offer discount:".format(developer))
            games = by_dev_with_disc(master_D, discount_D, developer)
            print(', '.join(games) if games else "Nothing to print")
        elif num == 7:
            print("\nThank you.")
            break
        else:
            print("\nInvalid option")
        num = int(input(MENU))

    pass   # remove this line

if __name__ == "__main__":
    main()