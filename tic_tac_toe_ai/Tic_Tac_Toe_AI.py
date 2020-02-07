"""
    Copy paste this entire code into http://www.codeskulptor.org/ and try 
    CodeSkulptor is an interactive, web-based Python programming environment that allows Python code to be run in a web browser.
    We follow Min-max algorithm in this code to play Tic-Tac-Toe with codeskulptor
"""

import poc_ttt_gui
import poc_ttt_provided as provided
import codeskulptor

# Set timeout, as mini-max can take a long time
codeskulptor.set_timeout(150)

# SCORING VALUES - DO NOT MODIFY
# player named PLAYERX who is going to us X
# player named PLAYERO who is going to us O

SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def make_move(board, player):
    """
    This method returns a tuple with 2 elements (row, col).
    The first element is the score 
    the second element is the desired move
    """
    winner = board.check_win()
    #base case
    if winner != None:
        #check winner and return score based on SCORES dictionary
        return (SCORES[winner], (-1,-1))
    #recursive case
    else:
        best_score = -10
        best_move = (-1,-1)
        empty_squares = board.get_empty_squares()

        for square in empty_squares:
            board_copy = board.clone()
            board_copy.move(square[0],square[1],player)
            
            result = make_move(board_copy, provided.switch_player(player))
            
            modified_score = result[0] * SCORES[player]

            if modified_score == 1:
                return result[0], square
            elif modified_score >= best_score:
                best_score = modified_score
                best_move = square
        return (SCORES[player] * best_score) , best_move
    

def move_wrapper(board, player, trials):

    move = make_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)
