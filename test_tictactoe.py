import unittest
from tictactoe import (
    X, O, EMPTY,
    initial_state, player,
    actions, result,
    winner, terminal,
    utility, minimax,
)


class TestBoards:
    @staticmethod
    def after_one_turn():
        return [[  X  , EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY],
                [EMPTY, EMPTY, EMPTY]]

    @staticmethod
    def X_win():
        return [[  X  ,   X  ,   X  ],
                [EMPTY,   O  , EMPTY],
                [EMPTY,   O  , EMPTY]]

    @staticmethod
    def O_win():
        return [[  O  ,   X  ,   X  ],
                [EMPTY,   O  , EMPTY],
                [  X  ,   X  ,   O  ]]


class PlayerTest(unittest.TestCase):
    def test_initial_state_turn(self):
        board = initial_state()
        expected_turn = X
        self.assertEqual(player(board), expected_turn)

    def test_second_turn(self):
        board = TestBoards.after_one_turn()
        expected_turn = O
        self.assertEqual(player(board), expected_turn)

    def test_second_turn_false(self):
        board = TestBoards.after_one_turn()
        expected_turn = X
        self.assertNotEqual(player(board), expected_turn)


class ActionsTest(unittest.TestCase):
    def test_initial_state_turn(self):
        board = initial_state()
        expected_actions = {
            (0, 0), (0, 1), (0, 2),
            (1, 0), (1, 1), (1, 2),
            (2, 0), (2, 1), (2, 2)
        }
        self.assertEqual(actions(board), expected_actions)

    def test_second_turn(self):
        board = TestBoards.after_one_turn()
        expected_actions = {
            (0, 1), (0, 2), (1, 0),
            (1, 1), (1, 2), (2, 0),
            (2, 1), (2, 2)
        }
        self.assertEqual(actions(board), expected_actions)


class ResultTest(unittest.TestCase):
    def test_first_turn_result(self):
        action = (1,1)
        board = TestBoards.after_one_turn()
        expected_board = [
            [  X  , EMPTY, EMPTY],
            [EMPTY,   O  , EMPTY],
            [EMPTY, EMPTY, EMPTY]
        ]
        self.assertEqual(result(board, action), expected_board)

    def test_invalid_input_result(self):
        action = (1,3)
        board = TestBoards.after_one_turn()
        self.assertRaises(Exception, result, board, action)


class WinnerTest(unittest.TestCase):
    def test_winner_top_row(self):
        board = TestBoards.X_win()
        expected_winner = X
        self.assertEqual(winner(board), expected_winner)


class TerminalTest(unittest.TestCase):
    def test_mid_gameplay(self):
        board = TestBoards.after_one_turn()
        expected_terminal = False
        self.assertEqual(terminal(board), expected_terminal)

    def test_terminal_board(self):
        board = TestBoards.X_win()
        expected_terminal = True
        self.assertEqual(terminal(board), expected_terminal)


class UtilityTest(unittest.TestCase):
    def test_draw_utility(self):
        board = TestBoards.after_one_turn()
        expected_utility = 0
        self.assertEqual(utility(board), expected_utility)

    def test_X_win_utility(self):
        board = TestBoards.X_win()
        expected_utility = 1
        self.assertEqual(utility(board), expected_utility)

    def test_O_win_utility(self):
        board = TestBoards.O_win()
        expected_utility = -1
        self.assertEqual(utility(board), expected_utility)


class MinimaxTest(unittest.TestCase):
    def test_terminal_board(self):
        board = TestBoards.X_win()
        expected_result = None
        self.assertEqual(minimax(board), expected_result)

    def test_second_turn_minimax(self):
        board = TestBoards.after_one_turn()
        expected_action = (1, 1)
        self.assertEqual(minimax(board), expected_action) 


if __name__ == '__main__':
    unittest.main()