#
# ps10pr3.py (Problem Set 10, Problem 3)
#
# Playing the game!
#
# name: Sirine Benbrahim
# email: sirineb@bu.edu 
#
# This is an individual-only problem that you must complete on your own,
# without a partner.
#

from ps10pr1 import Board
from ps10pr2 import Player
import random
    
def connect_four(player1, player2):
    """ Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                  players (objects of the Player class or a subclass of Player).
                  One of them should use 'X' checkers and the other should
                  use 'O' checkers.
    """
    # Make sure that one is 'X' and one is 'O'.
    if player1.checker not in 'XO' or player2.checker not in 'XO' \
       or player1.checker == player2.checker:
        print('need one X player and one O player.')
        return None

    print('Welcome to Connect Four!')
    print()
    board = Board(6, 7)
    print(board)
    
    while True:
        if process_move(player1, board):
            return board

        if process_move(player2, board):
            return board

def process_move(player, board):
    """takes two parameters: a Player object for the player whose move is being
       processed, and a Board object for the game that is being played; processes
       a single move by the specified player on the specified board"""
    print(player.__repr__() + "'s turn")
    move = player.next_move(board)
    board.add_checker(player.checker, move)
    print()
    print(board)
    print()
    if board.is_win_for(player.checker):
        print(player.__repr__() + ' ' + 'wins in' + ' ' + str(player.num_moves) + ' ' + 'moves.')
        print('Congratulations!')
        return True
    elif board.is_full():
        if not board.is_win_for(player.checker) and not board.is_win_for(player.opponent_checker()):
            print("It's a tie!")
            return True
    else:
        return False

class RandomPlayer(Player):
    """a blueprint for objects that represent an unintelligent computer player that
       chooses at random from the available columns; subclass of Player class"""

    def next_move(self, board):
        """overrides the next_move method that is inherited from Player; chooses at
           random from the columns in the specified board that are not yet full, and
           returns the index of that randomly selected column; increments the number
           of moves that the RandomPlayer"""
        columns_available = []
        for column in range(board.width):
            if board.can_add_to(column):
                columns_available += [column]

        self.num_moves += 1
        return random.choice(columns_available)