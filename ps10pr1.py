#
# ps10pr1.py (Problem Set 10, Problem 1)
#
# A Connect Four Board class
#
# name: Sirine Benbrahim
# email: sirineb@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

class Board:
    """a blueprint for objects that represent a Connect Four board; a data type for
       a Connect Four board with arbitrary dimensions"""

    def __init__(self, height, width):
        """a constructor for Board objects"""
        self.height = height
        self.width = width
        self.slots = [[' '] * width for row in range(self.height)]

    def __repr__(self):
        """returns a string representation of a Board object"""
        s = ''           # begin with an empty string

        # add one row of slots at a time
        for row in range(self.height):
            s += '|'     # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'    # newline at the end of the row
            
        # add hyphens at the bottom of the board
        s += '-' * (self.width * 2 + 1)
        s += '\n'

        # add the numbers underneath the board
        for i in range(self.width):
            s += ' ' + str(i % 10)

        return s

    def add_checker(self, checker, col):
        """accepts two inputs: checker, a one-character string that specifies the
           checker to add to the board (either 'X' or 'O') and col, an integer that
           specifies the index of the column to which the checker should be added
           and that adds checker to the appropriate row in column col of the board:
           adds the specified checker to column col of the called Board object.
        """
        assert(checker == 'X' or checker == 'O')
        assert(col >= 0 and col < self.width)

        row = self.height - 1
        while self.slots[row][col] != ' ':
            row -= 1

        self.slots[row][col] = checker

    def clear(self):
        """clears the Board object on which it is called by setting all slots to contain
           a space character."""
        for row in range(self.height):
            for col in range(self.width):
                self.slots[row][col] = ' '

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            
            # switch to the other bchecker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """returns True if it is valid to place a checker in the column col on the calling
           Board object. Otherwise, returns False; makes sure that col is in the range from
           0 to the last column on the board and that the specified column is not full."""
        if col < 0 or col >= self.width:
            return False
        elif self.slots[0][col] == 'X' or self.slots[0][col] == 'O':
            return False
        else:
            return True

    def is_full(self):
        """ returns True if the called Board object is completely full of checkers, and
            returns False otherwise."""
        for row in range(self.height):
            for col in range(self.width):
                if self.can_add_to(col):
                    return False
        return True

    def remove_checker(self, col):
        """removes the top checker from column col of the called Board object. If the
           column is empty, then the method does nothing."""
        row = 0
        while self.slots[row][col] == ' ' and row <= self.height:
            row += 1
            if row == self.height:
                row -= 1
                break

        if row <= self.height:
            self.slots[row][col] = ' '

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no vertical wins
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal win that goes down from left to right for the specified
            checker."""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True

        # if we make it here, there were no down diagonal wins
        return False

    def is_up_diagonal_win(self, checker):
        """ Checks for a diagonal win that goes up from left to right for the specified
            checker."""
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True

        # if we make it here, there were no up diagonal wins
        return False

    def is_win_for(self, checker):
        """accepts a parameter checker that is either 'X' or 'O', and returns True if
           there are four consecutive slots containing checker on the board. Otherwise,
           returns False."""
        assert(checker == 'X' or checker == 'O')

        if self.is_horizontal_win(checker):
            return True
        elif self.is_vertical_win(checker):
            return True
        elif self.is_down_diagonal_win(checker):
            return True
        elif self.is_up_diagonal_win(checker):
            return True
        else:
            return False
