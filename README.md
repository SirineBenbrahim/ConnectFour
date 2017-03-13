# ConnectFour
A connect four game in Python - there is even an AI Player option

  BoardClass.py:
     blueprint for objects that represent a Connect Four board with a width, height, and slots for each checker (2-D list)
     
  PlayerClass.py:
     blueprint for objects that represent a player in a Connect Four board game with a specified checker ('X' or 'O')
     
  RunGame.py:
     Plays a game of Connect Four between the two specified players,
        and returns the Board object as it looks at the end of the game.
        inputs: player1 and player2 are objects representing Connect Four
                players (objects of the Player class or a subclass of Player).
                One of them should use 'X' checkers and the other should
                use 'O' checkers.
    # Has a RandomPlayer class - a subclass of the Player class - that plays by choosing random columns to insert its checker
  AIPLayer.py:
    subclass of Player class : looks ahead some number of moves into the future to assess the impact
       of each possible move that it could make for its next move, and assigns
       a score to each possible move; since each move corresponds to a column
       number, it effectively assigns a score to each column; chooses as its next
       move the column with the maximum score (this is the player’s judgment of
       its best possible move)
       
AIPlayer Class:
  Has attributes including: 
    1.) checker : whether its checker is 'X' or 'O'
    2.) tiebreak : in the AIPlayer's strategy, specifies how to break ties when deciding which column to pick when the scores                    for certain columns are the same; either 'LEFT' to choose rightmost column with the highest score, 'RIGHT'                    to choose rightmost column with the highest score, or 'RANDOM" to choose a random column with the highest                      score
    3.) lookahead : an integer specifying how many moves the player looks ahead in order to evaluate possible moves                               (recommended lookahead: around 3) 


To play against another person:
  Run "RunGame.py" file
  Enter commands:
    >>> player1 = Player('X')  # player1 has the 'X' checker
    >>> player2 = Player('O')  # player2 has the 'O' checker
    >>> connect_four(player1, player2)
    # The player with the 'X' checker always goes first
    # Play the game!
    
To play against an unintelligent computer:
  Run "RunGame.py" file
  Enter commands:
    >>> player1 = Player('X')  # player1 has the 'X' checker
    >>> player2 = RandomPlayer('O')  # player2 has the 'O' checker
    >>> connect_four(player1, player2)
    # The player with the 'X' checker always goes first
    # Play the game!
    
To play against the AI player:
  Run "AIPlayer.py" file
  Enter commands:
    >>> player1 = Player('X')  # player1 has the 'X' checker
    >>> player2 = AIPlayer('O', 'RANDOM', 3)  # player2, the AI player, has the 'O' checker, 'RANDOM' tiebreak, 
                                              # and lookahead of 3 moves
    >>> connect_four(player1, player2)
    # The player with the 'X' checker always goes first
    # Play the game!
