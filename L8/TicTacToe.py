# Tic-Tac-Toe
# Plays the game of tic-tac-toe against a human opponent

BOARD_SIZE = 9


def ask_question(question, low=None, high=None):
    response = None

    if not low and not high:

        while response not in ("y", "n"):
            response = raw_input(question).lower()

    else:

        while response not in range(low, high):
            try:
                response = int(raw_input(question))

                if response not in range(low, high):
                    print("HA! That's not a valid move")

            except ValueError:
                print("That's not a number. Try again")
                continue

    return response


def who_on_first():

    first_play = ask_question("Would you like to go first? (y/n): ")

    if first_play == "y":

        print("Fine, go for it")
        human = "X"
        computer = "O"

    else:

        print("Interesting, here I come")
        computer = "X"
        human = "O"

    return computer, human


def empty_board():

    board = []

    for space in range(BOARD_SIZE):
        board.append("")

    return board


def display_board(board):
    print(board[0], "|", board[1], "|", board[2])
    print("-------------------------")
    print(board[3], "|", board[4], "|", board[5])
    print("-------------------------")
    print(board[6], "|", board[7], "|", board[8])


def moves(board):
    moves = []
    for square in range(BOARD_SIZE):
        if board[square] == "":
            moves.append(square)
    return moves


def winner(board):
    WAYS_TO_WIN = ((0, 1, 2),
                   (3, 4, 5),
                   (6, 7, 8),
                   (0, 3, 6),
                   (1, 4, 7),
                   (2, 5, 8),
                   (0, 4, 8),
                   (2, 4, 6))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != "":
            winner = board[row[0]]
            return winner

    if "" not in board:
        return "TIE"

    return None


def human_move(board):

    legal = moves(board)
    move = None

    while move not in legal:

        move = ask_question("Choose your move (0 - 8):", 0, BOARD_SIZE)

        if move not in legal:
            print("That space is already occupied.  Choose another.")

    return move


def computer_move(board, computer, human):
    """Make computer move."""
    # make a copy to work with since function will be changing list
    board = board[:]
    # the best positions to have, in order
    BEST_MOVES = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("I shall take square number")

    # if computer can win, take that move
    for move in moves(board):
        board[move] = computer
        if winner(board) == computer:
            print(move)
            return move
        # done checking this move, undo it
        board[move] = ""

    # if human can win, block that move
    for move in moves(board):
        board[move] = human
        if winner(board) == human:
            print(move)
            return move
        # done checkin this move, undo it
        board[move] = ""

    # since no one can win on next move, pick best open square
    for move in BEST_MOVES:
        if move in moves(board):
            print(move)
            return move


def next_turn(turn):
    if turn == "X":
        return "O"
    else:
        return "X"


def identify_winner(the_winner, computer, human):
    if the_winner == computer:
        print("I win. You loose. Nice try")

    elif the_winner == human:
        print("You won the battle but not the war.")

    elif the_winner == "TIE":
        print("Impressive, you would make a good computer")

def main():
    print(
        """
        Human, I challenge you to a good old fashioned tic tac toe game. You shall
        select a number corresponding to the position in the board as illustrated:

                        0 | 1 | 2
                        ---------
                        3 | 4 | 5
                        ---------
                        6 | 7 | 8

        Good luck, human.
        """
    )
    computer, human = who_on_first()
    turn = "X"
    board = empty_board()
    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board)
            board[move] = human
        else:
            move = computer_move(board, computer, human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    identify_winner(the_winner, computer, human)

# start the program
main()