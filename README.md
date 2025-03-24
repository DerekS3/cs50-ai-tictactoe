# CS50 AI Tic-Tac-Toe

This project implements a Tic-Tac-Toe game with an AI opponent that uses the minimax algorithm to play optimally. The game allows a human player to compete against the AI, and the AI ensures that it either wins or results in a tie if both players play perfectly.

## Contributions

within tic-tac-toe.py
#player: Determines which player's turn it is (X or O) based on the current board state. Alternates between players after each move.
actions: Returns a set of all possible moves (represented as tuples) that can be made on the current board, excluding cells already occupied by X or O.
result: Generates a new board state after a valid move, without modifying the original board. Raises an exception for invalid moves.
winner: Identifies the winner (X or O) if three of the same symbols are aligned horizontally, vertically, or diagonally. Returns None if there is no winner.
terminal: Checks if the game is over by determining if a player has won or all cells are filled. Returns True if the game is finished, otherwise False.
utility: Calculates the utility of a terminal board. Returns 1 if X wins, -1 if O wins, and 0 for a tie.
minimax: Implements the minimax algorithm to determine the optimal move for the current player. Returns None if the game is over.

### Test Suite
The test suite `test_tictactoe.py` was built using Python's `unittest` framework to verify the correctness of the Tic-Tac-Toe logic and ensure that the AI behaves as expected.

