"""
This file was created by Joaquin Escalante Canto
The program allows a player to play a game of TicTacToe versus and AI
"""

# Set board size for tic tac toe, allow flexibility for other games
BOARD_SIZE = 9


def ask_question(question, low=None, high=None):
    """
    :param question: string of the question that must be answered by player
    :param low: The lower value accepted for a move
    :param high: The upper value accepted for a move
    :return: validated input response
    """
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
    """
    :return: The shape that will be using the computer and human
    """

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
    """
    Create empty list of the size of board
    :return: list
    """
    board = []

    for space in range(BOARD_SIZE):
        board.append("")

    return board


def display_board(board):
    """
    Display current state of board
    :param board: list representation of the board
    :return:
    """
    print(board[0], "|", board[1], "|", board[2])
    print("-------------------------")
    print(board[3], "|", board[4], "|", board[5])
    print("-------------------------")
    print(board[6], "|", board[7], "|", board[8])


def moves(board):
    """
    Create list of available moves, spaces that haven't been occupied
    :param board:
    :return: list of moves
    """
    moves = []
    for square in range(BOARD_SIZE):
        if board[square] == "":
            moves.append(square)
    return moves


def winner(board):
    """
    Define winning combinations and check state of the board to find winner
    :param board:
    :return: Returns the winning shape (X or O) if any, otherwise return TIE or None
    """
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


def player_move(board):
    """
    Receive human input and verify it
    :param board:
    :return: the index of valid selected space
    """
    legal = moves(board)
    move = None

    while move not in legal:

        move = ask_question("Choose your move (0 - 8):", 0, BOARD_SIZE)

        if move not in legal:
            print("That space is already occupied.  Choose another.")

    return move


def computer_move(board, computer, human):
    """
    This function will analyze best next move for computer. It will check if computer can win with next move and choose
    that space, if human can win next turn it will block that space, if no win next turn it will select best move
    from predetermined list of moves
    :param board: Current state of board
    :param computer: Computer shape (X or O)
    :param human: Human shape (X or O)
    :return: index of selected next move
    """
    board = board[:]
    best_move = (4, 0, 2, 6, 8, 1, 3, 5, 7)

    print("Let me think..I choose:")

    # Take winning move if any otherwise undo it
    for move in moves(board):
        board[move] = computer

        if winner(board) == computer:
            print(move)

            return move

        board[move] = ""

    # Block winning move if any otherwise undo it
    for move in moves(board):
        board[move] = human

        if winner(board) == human:
            print(move)

            return move

        board[move] = ""

    # Select best next move
    for move in best_move:
        if move in moves(board):
            print(move)
            return move


def next_turn(turn):
    """
    Change shape to be used for filling selected space since its a turn based game
    :param turn: Current shape in turn
    :return: Opposite shape
    """
    if turn == "X":
        return "O"
    else:
        return "X"


def identify_winner(the_winner, computer, human):
    """
    Tell player who won game or if it was a tie
    :param the_winner: String representation of winning shape or TIE
    :param computer: String representation of shape used by computer
    :param human: String representation of shape used by human
    :return:
    """
    if the_winner == computer:
        print("I win. You loose. Nice try")

    elif the_winner == human:
        print("You won the battle but not the war.")

    elif the_winner == "TIE":
        print("It's a Tie. Impressive, you would make a good computer")


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
            move = player_move(board)
            board[move] = human

        else:
            move = computer_move(board, computer, human)
            board[move] = computer

        display_board(board)
        turn = next_turn(turn)

    the_winner = winner(board)
    identify_winner(the_winner, computer, human)


# Start game
main()
