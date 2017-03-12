#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# An AI Player for Connect Four
#
# name: Sirine Benbrahim
# email: sirineb@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name:
# partner's email:
#

from ps10pr3 import *
import random

class AIPlayer(Player):
    """looks ahead some number of moves into the future to assess the impact
       of each possible move that it could make for its next move, and assigns
       a score to each possible move; since each move corresponds to a column
       number, it effectively assigns a score to each column; chooses as its next
       move the column with the maximum score; this is the player’s judgment of
       its best possible move; subclass of Player class"""

    def __init__(self, checker, tiebreak, lookahead):
        """calls Player constructor to initialize most of the attributes; initializes
           other attributes including tiebreak, that stores a string specifying the
           player’s tiebreaking strategy ('LEFT', 'RIGHT', or 'RANDOM') and lookahead,
           that stores an integer specifying how many moves the player looks ahead in
           order to evaluate possible moves"""
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        Player.__init__(self, checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """overrides __repr__ method that is inherited from Player; returns a string
           representing an AIPlayer object; indicates which checker the AIPlayer object
           is using, indicates the player’s tiebreaking strategy and lookahead"""
        s = 'Player' + ' ' + self.checker + ' ' + '(' + self.tiebreak + ',' + ' ' + str(self.lookahead) + ')' 

        return s

    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board and returns
           the index of the column with the maximum score (if one or more columns are tied
           for the maximum score, then applies the called AIPlayer‘s tiebreaking strategy to
           break the tie"""
        maximum_score = max(scores)
        list_max_scores = []
        for i in range(len(scores)):
            if scores[i] == maximum_score:
                list_max_scores += [i]
        if self.tiebreak == 'RANDOM':
            index = random.choice(list_max_scores)
        elif self.tiebreak == 'LEFT':
            index = list_max_scores[0]
        elif self.tiebreak == 'RIGHT':
            index = list_max_scores[-1]
        return index

    def scores_for(self, board):
        """takes a Board object board and determines the called AIPlayer‘s scores for the
           columns in board; each column is assigned one of four possible scores based on
           the called AIPlayer‘s lookahead value; returns a list containing one score for
           each column"""
        scores = [50] * board.width
        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                board.add_checker(self.checker, col)
                opp_AI_player = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp_AI_player.scores_for(board)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """overrides the next_move that is inherited from Player; returns the called AIPlayer‘s
           judgment of its best possible move"""
        scores = self.scores_for(board)
        index = self.max_score_column(scores)
        self.num_moves += 1
        return index
