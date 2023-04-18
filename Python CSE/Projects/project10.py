import cards  # required !!!

RULES = '''
Aces High Card Game:
     Tableau columns are numbered 1,2,3,4.
     Only the card at the bottom of a Tableau column can be moved.
     A card can be moved to the Foundation only if a higher ranked card 
     of the same suit is at the bottom of another Tableau column.
     To win, all cards except aces must be in the Foundation.'''

MENU = '''     
Input options:
    D: Deal to the Tableau (one card on each column).
    F x: Move card from Tableau column x to the Foundation.
    T x y: Move card from Tableau column x to empty Tableau column y.
    R: Restart the game (after shuffling)
    H: Display the menu of choices
    Q: Quit the game        
'''

def init_game():
    stock = cards.Deck()
    stock.shuffle()

    # Create the tableau with 4 empty columns
    tableau = [[] for _ in range(4)]

    # Deal one card to each tableau column
    for col in tableau:
        col.append(stock.deal())

    # Initialize the foundation as an empty list
    foundation = []

    return stock, tableau, foundation

    
def deal_to_tableau( tableau, stock):
    for col in tableau:
        if not stock.is_empty():
            col.append(stock.deal())
        else:
            break

           
def validate_move_to_foundation( tableau, from_col ):
    if not tableau[from_col]:  # Check if the column is empty
        print("\nError, empty column: {}".format(from_col + 1))
        return False

    card_to_move = tableau[from_col][-1]  # Get the bottom card of the column

    if card_to_move.rank() == 1:  # Check if the card is an Ace (rank 1 in the cards module)
        print("\nError, cannot move {}.".format(card_to_move))
        return False

    other_cards = [col[-1] for i, col in enumerate(tableau) if i != from_col and col]

    max_rank = 0
    for card in other_cards:
        if card.suit() == card_to_move.suit():
            max_rank = max(max_rank, card.rank())

    if card_to_move.rank() > max_rank:
        return True
    else:
        print("\nError, cannot move {}.".format(card_to_move))
        return False


    
def move_to_foundation( tableau, foundation, from_col ):
    if not tableau[from_col]:  # Check if the column is empty
        return

    card_to_move = tableau[from_col][-1]  # Get the bottom card of the column

    if card_to_move.rank() == 1:  # Check if the card is an Ace (rank 1 in the cards module)
        return

    for col in tableau:
        if col and col[-1].suit() == card_to_move.suit() and col[-1].rank() > card_to_move.rank():
            tableau[from_col].pop()
            foundation.append(card_to_move)
            return


def validate_move_within_tableau( tableau, from_col, to_col ):
    # Check if the columns are within the range
    if from_col < 0 or from_col > 3 or to_col < 0 or to_col > 3:
        return False

    # Check if there is a card in the from_col
    if not tableau[from_col]:
        print(f"Error, no card in column: {from_col}")
        return False

    # Check if the target column (to_col) is empty
    if tableau[to_col]:
        print(f"Error, target column is not empty: {to_col}")
        return False

    return True


def move_within_tableau( tableau, from_col, to_col ):
    if not tableau[from_col]:  # Check if the from_col is empty
        return

    if tableau[to_col]:  # Check if the to_col is not empty
        return

    card_to_move = tableau[from_col][-1]  # Get the bottom card of the from_col
    tableau[from_col].pop()  # Remove the card from the from_col
    tableau[to_col].append(card_to_move)  # Add the card to the to_col
        
def check_for_win( tableau, stock ):
    if stock:
        return False

    # Check if the tableau has the four aces in the first position of each column
    aces = ["A♥", "A♦", "A♣", "A♠"]
    for col in tableau:
        if not col or col[0] not in aces:
            return False
        aces.remove(col[0])

    return True
    
def display( stock, tableau, foundation ):
    '''Provided: Display the stock, tableau, and foundation.'''

    print("\n{:<8s}{:^13s}{:s}".format( "stock", "tableau", "  foundation"))
    maxm = 0
    for col in tableau:
        if len(col) > maxm:
            maxm = len(col)
    
    assert maxm > 0   # maxm == 0 should not happen in this game?
        
    for i in range(maxm):
        if i == 0:
            if stock.is_empty():
                print("{:<8s}".format(""),end='')
            else:
                print("{:<8s}".format(" XX"),end='')
        else:
            print("{:<8s}".format(""),end='')        
        
        #prior_ten = False  # indicate if prior card was a ten
        for col in tableau:
            if len(col) <= i:
                print("{:4s}".format(''), end='')
            else:
                print( "{:4s}".format( str(col[i]) ), end='' )

        if i == 0:
            if len(foundation) != 0:
                print("    {}".format(foundation[-1]), end='')
                
        print()


def get_option():
    user_input = input("\nInput an option (DFTRHQ): ").upper()

    if user_input == "D":
        return ["D"]
    elif user_input.startswith("F "):
        try:
            x = int(user_input[2:])
            return ["F", x]
        except ValueError:
            print("\nError in option:")
            return []
    elif user_input.startswith("T "):
        try:
            x, y = map(int, user_input[2:].split())
            return ["T", x, y]
        except ValueError:
            print("\nError in option:")
            return []
    elif user_input == "R":
        return ["R"]
    elif user_input == "H":
        return ["H"]
    elif user_input == "Q":
        return ["Q"]
    else:
        print("\nError in option:")
        return []

def main():
    print(RULES)
    print(MENU)

    stock, tableau, foundation = init_game()
    display(stock, tableau, foundation)

    while True:
        option = get_option()

        if option[0] == "D":
            deal_to_tableau(tableau, stock)
            display(stock, tableau, foundation)
        elif option[0] == "F":
            from_col = option[1] - 1
            if validate_move_to_foundation(tableau, from_col):
                move_to_foundation(tableau, foundation, from_col)
                display(stock, tableau, foundation)
        elif option[0] == "T":
            from_col, to_col = option[1] - 1, option[2] - 1
            if validate_move_within_tableau(tableau, from_col, to_col):
                move_within_tableau(tableau, from_col, to_col)
                display(stock, tableau, foundation)
        elif option[0] == "R":
            print("=========== Restarting: new game ============")
            stock, tableau, foundation = init_game()
            display(stock, tableau, foundation)
        elif option[0] == "H":
            print(MENU)
        elif option[0] == "Q":
            print("\nYou have chosen to quit.")
            break

        if check_for_win(tableau, stock):
            print("\nYou won!")
            break

if __name__ == '__main__':
     main()