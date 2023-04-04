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
    ''' Docstring'''
    while True:
        file_name = input(f"Please enter the name of the {s} file: ")
        try:
            fp = open(file_name, "r", encoding="UTF-8")
            return fp
        except FileNotFoundError:
            print(f"Error: {file_name} not found. Please try again.")
        except:
            print("Error: unable to open file. Please try again.")

def read_file(fp_games):
    ''' Docstring'''
    next(fp_games)

    games_dict = {}

    for row in csv.reader(fp_games):
        name = row[0]
        date = row[1]
        developer = row[2].split(';')
        genres = row[3].split(';')
        mode = 0 if 'single-player' in row[4].lower() else 1
        price = row[5].replace(',', '')
        try:
            price = float(price) * 0.012
        except ValueError:
            price = 0.0
        overall_reviews = row[6]
        reviews = int(row[7])
        percent_positive = int(row[8].replace('%', ''))
        support = ['win_support' if row[9] == '1' else '',
                   'mac_support' if row[10] == '1' else '',
                   'lin_support' if row[11] == '1' else '']

        games_dict[name] = [date, developer, genres, mode, price, overall_reviews, reviews, percent_positive, support]

    return games_dict
    pass   # remove this line

def read_discount(fp_discount):
    ''' Docstring'''
    discount_dict = {}

    # Skip the header line
    fp_discount.readline()

    for line in fp_discount:
        # Split the line into its comma-separated values
        values = line.strip().split(',')
        
        # Check if the line has at least 5 values
        if len(values) >= 5:
            game_name, _, _, discount_perc, _ = values
            # Add the game name and discount percentage to the dictionary
            discount_dict[game_name] = round(float(discount_perc), 2)

    return discount_dict
    pass   # remove this line

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

    filtered_games = []
    for game in master_D:
        if genre in master_D[game][2]:
            if master_D[game][5] == 'Positive':
                filtered_games.append((game, float(master_D[game][4].replace(',', '')), master_D[game][0]))

    filtered_games.sort(key=lambda x: (-x[1], x[2]))

    return [game[0] for game in filtered_games]
    pass   # remove this line
        
def by_dev(master_D,developer): 
    ''' Docstring'''
    games_by_dev = []
    for game, info in master_D.items():
        if developer in info[1]:
            games_by_dev.append(game)
    sorted_games = sorted(games_by_dev, key=lambda x: (master_D[x][1], x))
    return sorted_games[::-1]
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
    result = []
    for game, details in master_D.items():
        if genre in details[2] and details[4] == 0:
            if game in discount_D:
                continue
            result.append((game, details[4]))
    return [game for game, _ in sorted(result, key=lambda x: x[1])]
    pass   # remove this line

def by_dev_with_disc(master_D,discount_D,developer):
    ''' Docstring'''
    # Filter out games by the specified developer and apply discounts
    games = [game for game, details in master_D.items() if developer in details[1]]
    discounted_games = {game: details[4] - discount_D.get(game, 0) for game, details in master_D.items() if game in games}

    # Sort games by price from cheapest to most expensive
    sorted_games = sorted(discounted_games.items(), key=lambda x: x[1])

    # Return a list of game names
    return [game for game, price in sorted_games]
    pass   # remove this line
    
             
def main():
    pass   # remove this line

if __name__ == "__main__":
    main()