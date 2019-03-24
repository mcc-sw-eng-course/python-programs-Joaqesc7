from unittest import TestCase, main
from unittest.mock import patch
import TicTacToe as ttt

class TestTicTac(TestCase):

    @patch('TicTacToe.ask_question', return_value='yes')
    def test_answer_yes(self, input):
        self.assertEqual(ttt.who_on_first(), ('O', 'X'))

    @patch('TicTacToe.ask_question', return_value='no')
    def test_answer_no(self, input):
        self.assertEqual(ttt.who_on_first(), ('X', 'O'))

    def test_empty_board(self):
        self.assertEqual(ttt.empty_board(), ['', '', '', '', '', '', '', '', ''])

    def test_moves(self):
        board = ttt.empty_board()
        self.assertEqual(ttt.moves(board), [0, 1, 2, 3, 4, 5, 6, 7, 8])

    @patch('TicTacToe.ask_question', return_value=0)
    def test_valid_input(self, input):
        board = ttt.empty_board()
        self.assertEqual(ttt.player_move(board), 0)

    def test_computer_winning_move(self):
        board = ['X', 'X', '', 'O', '', '', 'O', '', '']
        self.assertEqual(ttt.computer_move(board, 'X', 'O'), 2)

    def test_computer_blocking_move(self):
        board = ['X', 'X', '', 'O', '', '', 'O', '', '']
        self.assertEqual(ttt.computer_move(board, 'O', 'X'), 2)

    def test_computer_best_move(self):
        board = ['', '', '', '', '', '', '', '', '']
        self.assertEqual(ttt.computer_move(board, 'O', 'X'), 4)

    def test_next_turn(self):
        self.assertEqual(ttt.next_turn('X'), 'O')

    def test_next_turn_X(self):
        self.assertEqual(ttt.next_turn('O'), 'X')

    def test_win_computer(self):
        self.assertEqual(ttt.identify_winner('X', 'X', 'O'), None)

    def test_win_human(self):
        self.assertEqual(ttt.identify_winner('X', 'O', 'X'), None)

    def test_tie(self):
        self.assertEqual(ttt.identify_winner('TIE', 'O', 'X'), None)

    def test_display_board(self):
        board = ['', '', '', '', '', '', '', '', '']
        self.assertEqual(ttt.display_board(board), None)

    @patch('TicTacToe.ask_question', return_value="yes")
    def test_answer_yes_method(self, input):
        self.assertEqual(ttt.ask_question('test'), 'yes')

    @patch('TicTacToe.ask_question', return_value=1)
    def test_answer_int_method(self, input):
        self.assertEqual(ttt.ask_question('test', 0, 8), 1)



if __name__ == '__main__':
    main()
