""" Mancala app. """

from random import choice

from .constants import DEFAULT_NAME, RANDOM_AI, VECTOR_AI, DEFAULT_AI, \
    P1_PITS, P2_PITS
from .board import Board, InvalidMove

class Match(object):
    """ A match of Mancala has two Players and a Board.

    Match tracks current turn.

    """

    def __init__(self):
        """ Initializes a new match. """
        self.players = [Player(1), AIPlayer(2)]
        self.player1 = self.players[0]
        self.player2 = self.players[1]
        self.current_turn = self.player1
        self.board = Board()

    def handle_next_move(self):
        """ Shows board and handles next move. """
        self.board.textify_board()

        next_move = self.current_turn.get_next_move()
        try:
            self.board._move_stones(self.current_turn.number, next_move)
        except InvalidMove:
            if self.current_turn.__class__ == HumanPlayer:
                print "Please select a move with stones you can move."
            self.handle_next_move()

        # Check whether game was won.
        if self._check_for_winner():
            import sys
            sys.exit()

        # Check whether free move was earned
        if self.board._move_stones(
            self.current_turn.number,
            next_move, check_free_move=True
            ):
            print "Free move earned!"
            self.handle_next_move()
        else:
            self._swap_current_turn()
            self.handle_next_move()


    def _swap_current_turn(self):
        """ Swaps current turn to the other player. """
        if self.current_turn == self.player1:
            self.current_turn = self.player2
            return self.player2
        else:
            self.current_turn = self.player1
            return self.player1

    def _check_for_winner(self):
        """ Checks for winner. Announces the win."""
        if set(self.board.board[P1_PITS]) == set([0]):
            print "Player 1 wins!"
            return True
        elif set(self.board.board[P2_PITS]) == set([0]):
            print "Player 2 wins!"
            return True
        else:
            return False


class Player(object):
    """ A player of Mancala. """

    def __init__(self, number=None, name=DEFAULT_NAME):
        self.name = name
        self.number = number

    def __str__(self):
        return "Player: %s" % self.name

    def get_name(self):
        """ Returns player name. """
        return self.name

class HumanPlayer(Player):
    """ A human player. """

    def __init__(self, name=None):
        super(HumanPlayer, self).__init__()
        if name:
            self.name = name
        else:
            self.name = self.get_human_name()

    def get_human_name(self):
        """ Asks human players to specify their name. """
        return raw_input("Please input your name: ")

    def get_next_move(self):
        """ Gets next move from a human player. """
        return input("Please input your next move (0 to 5): ")



class AIPlayer(Player):
    """ Base class for an AI Player """
    def __init__(self, ai_profile=None):
        """ Initializes an AI profile. """
        if ai_profile:
            self.ai_profile = ai_profile
        else:
            self.ai_profile = DEFAULT_AI

    def get_next_move(self):
        """ Returns next AI move based on profile. """
        if self.ai_profile == RANDOM_AI:
            return choice(range(0, 5))
        elif self.ai_profile == VECTOR_AI:
            pass
            # TODO(anuzis): use thoughtful way to instantiate classes that
            # inherit from AI_Profile.
