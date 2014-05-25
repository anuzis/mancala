""" Mancala app. """

from random import choice

from .constants import DEFAULT_NAME, RANDOM_AI, VECTOR_AI, DEFAULT_AI, \
    P1_PITS, P2_PITS, P1_STORE, P2_STORE
from .board import Board, InvalidMove

class Player(object):
    """ A player of Mancala. """

    def __init__(self, number=None, board=None, name=DEFAULT_NAME):
        self.name = name
        self.number = number
        self.board = board

    def __str__(self):
        return "Player: %s" % self.name

    def get_name(self):
        """ Returns player name. """
        return self.name

class Match(object):
    """ A match of Mancala has two Players and a Board.

    Match tracks current turn.

    """

    def __init__(self, player1_type=Player, player2_type=Player):
        """ Initializes a new match. """
        self.board = Board()
        self.players = [player1_type(1, self.board), player2_type(2, self.board)]
        self.player1 = self.players[0]
        self.player2 = self.players[1]
        self.current_turn = self.player1

    def handle_next_move(self):
        """ Shows board and handles next move. """
        print self.board.textify_board()

        next_move = self.current_turn.get_next_move()
        try:
            self.board.board, free_move_earned = self.board._move_stones(self.current_turn.number, next_move)
        except InvalidMove:
            # Check whether game was won by AI.
            if self._check_for_winner():
                import sys
                sys.exit()
            if self.current_turn.__class__ == HumanPlayer:
                print "Please select a move with stones you can move."
            self.handle_next_move()

        # Check whether game was won.
        if self._check_for_winner():
            import sys
            sys.exit()

        # Check whether free move was earned
        if free_move_earned:
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
            print "Player 1 finished! P1: %d to P2: %d" % (self.board.board[P1_STORE][0], self.board.board[P2_STORE][0])
            return True
        elif set(self.board.board[P2_PITS]) == set([0]):
            print "Player 2 finished! P1: %d to P2: %d" % (self.board.board[P1_STORE][0], self.board.board[P2_STORE][0])
            return True
        else:
            return False

class HumanPlayer(Player):
    """ A human player. """

    def __init__(self, number, board, name=None):
        super(HumanPlayer, self).__init__(number, board)
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
    def __init__(self, number, board, ai_profile=None):
        """ Initializes an AI profile. """
        super(AIPlayer, self).__init__(number, board)
        if ai_profile:
            self.ai_profile = ai_profile
        else:
            self.ai_profile = DEFAULT_AI

    def _get_eligible_moves(self):
        """ Returns a list of integers representing eligible moves. """
        
        if self.number == 1:
            pits = self.board.board[P1_PITS]
        else:
            pits = self.board.board[P2_PITS]

        eligible_moves = []
        for i in range(len(pits)):
            if not pits[i] == 0:
                eligible_moves.append(i)

        return eligible_moves


    def get_next_move(self):
        """ Returns next AI move based on profile. """

        import time
        print "AI is thinking..."
        #time.sleep(5)

        eligible_moves = self._get_eligible_moves()

        if self.ai_profile == RANDOM_AI:
            return choice(eligible_moves)
        elif self.ai_profile == VECTOR_AI:
            pass
            # TODO(anuzis): use thoughtful way to instantiate classes that
            # inherit from AI_Profile.
