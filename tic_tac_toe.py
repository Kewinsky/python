# Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-", ]

# If game is still going
game_still_going = True

# Who's the winner ?!
winner = None

# Who's trun now ?!
current_player = "x"


# Display the board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# --------------------------------------------------------#
# Start the game :)
def play_game():
    # Display initial board
    display_board()
    while game_still_going:
        # handle a single turn of an arbitrary player
        handle_turn(current_player)

        # check if the game has ended
        check_is_game_over()

        # flip to the other player
        flip_player()

    # The game has ended
    if winner == "x" or winner == "o":
        print("The winner is: " + str(winner))
    elif winner == None:
        print("We have a tie :|")


def flip_player():
    # global variables we need
    global current_player
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player = "x"
    return


def check_is_game_over():
    global check_if_tie
    check_for_winner()
    check_if_tie


def check_if_tie():
    global  game_still_going
    if "-" not in board:
        game_still_going = False

    return


def check_for_winner():

    # set up global winner
    global winner

    # Check_rows
    row_winner = check_rows()
    # Check_columns
    column_winner = check_columns()
    # Check_diagonals
    diagonal_winner = check_diagonals()
    if row_winner:
        # win
        winner = row_winner
    elif column_winner:
        # win
        winner = column_winner
    elif diagonal_winner:
        # win
        winner = diagonal_winner
    else:
        # no win
        winner = None
    return

def check_rows():
    # set up global variables
    global game_still_going
    # chceck if any of the rows have all the same value ( no '-' )
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    # if any row does have a match, flag that there is a win
    if row_1 or row_2 or row_3:
        game_still_going = False
    # Return the winner
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # set up global variables
    global game_still_going
    # chceck if any of the rows have all the same value ( no '-' )
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    # if any row doeas have a match, flag tht there is a win
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    # set up global variables
    global game_still_going
    # chceck if any of the rows have all the same value ( no '-' )
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    # if any row doeas have a match, flag tht there is a win
    if diagonal_1 or diagonal_2:
        game_still_going = False

    # Return the winner
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[1]
    return


def handle_turn(current_player):
    print(current_player + "'s turn.")
    position = input("Choose a position from 1-9: ")
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose a position from 1-9: ")
        position = int(position) - 1  # po to zeby mozna było wybrać numer 1-9 a nie 0-8

        if board[position] == "-":
            valid = True
        else:
            print("You can't go there. Go again.")

    board[position] = current_player
    display_board()

play_game()
