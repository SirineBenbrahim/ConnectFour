#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect Four Player class 
#
# name: Sirine Benbrahim
# email:
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from ps10pr1 import Board

class Player:
    """a blueprint for objects that represent a player in a Connect Four board game"""

    def __init__(self, checker):
        """a constructor for Player objects"""
        assert(checker == 'X' or checker == 'O')

        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """returns a string representing a Player object. The string returned indicates
          which checker the Player object is using."""
        return 'Player' + ' ' + self.checker

    def opponent_checker(self):
        """returns a one-character string representing the checker of the Player object’s
           opponent."""
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """accepts a Board object as a parameter and returns the column where the player
           wants to make the next move."""
        column = int(input('Enter a column: '))

        while not board.can_add_to(column):
            print('Try again!')
            column = int(input('Enter a column: '))

        self.num_moves += 1
        return column
