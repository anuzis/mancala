""" Mancala app. """

from random import choice

from .constants import P1_PITS, P1_STORE, P2_PITS, P2_STORE, \
    DEFAULT_NAME, RANDOM_AI, VECTOR_AI, DEFAULT_AI

class InvalidBoardArea(Exception):
    """ Exception flagged when moves are attempted on an unknown area. """
    pass

class TooManyPlayers(Exception):
    """ Exception flagged when more than 2 players are created. """
    pass

class MatchMaker(object):
    """ Makes a new match of Mancala and handles game flow. """

    human_wins = 0
    ai_wins = 0

    def __init__(self, current_turn=1):
        self.player1 = Player()
        self.player2 = Player()
        self.board = Board()
        self.current_turn = current_turn

    def get_current_turn_and_swap(self):
        """ Returns an integer corresponding with the current player's turn.
        Swaps current turn to the other player. """
        if self.current_turn == 1:
            self.current_turn = 2
            return 1
        else:
            self.current_turn = 1
            return 2

    def check_for_winner(self):
        """ Checks for winner. Announces the win and records stats."""
        pass


class Player(object):
    """ A player of Mancala. """

    player_count = 0

    def __init__(self, name=DEFAULT_NAME):
        self.__class__.player_count += 1

        if self.__class__.player_count > 2:
            raise TooManyPlayers

        self.number = self.player_count
        self.name = name

    def __str__(self):
        return "Player: %s" % self.name

    def get_name(self):
        """ Returns player name. """
        return self.name

    def get_number(self):
        """ Returns player number. """
        return self.number

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
            return choice(range(0,5))
        elif self.ai_profile == VECTOR_AI:
            pass
            # TODO(anuzis): use thoughtful way to instantiate classes that
            # inherit from AI_Profile.

class Board(object):
    """ A Mancala board with size pockets per player and stones """

    def __init__(self, pits=6, stones=4, test_state=None):
        if test_state:
            self.board = test_state
        else:
            self.board = [[stones] * pits, [0], [stones] * pits, [0]]

    def textify_board(self):
        """ Returns the current board as a printable string to show the user.

        Note that the order of player 2 pits are displayed in reverse
        from the list index to give the appearance of a loop.
        """
        return "   %d  %d  %d  %d  %d  %d\n %d                    %d\n   %d  %d  %d  %d  %d  %d\n" % (
                       # Player 2 pits in top row
                       self.board[2][5], self.board[2][4], self.board[2][3],
                       self.board[2][2], self.board[2][1], self.board[2][0],
                       # Player 2 & 1 stores in middle row
                       self.board[3][0], self.board[1][0],
                       # Player 1 pits on bottom row
                       self.board[0][0], self.board[0][1], self.board[0][2],
                       self.board[0][3], self.board[0][4], self.board[0][5])

    def move_stones(self, player, start_index):
        """ Moves stones by the given Player, starting at the given index.
        Returns finished state of the Board.

        board: current instance of Board class
        player: instance of Player class
        start_index: integer
        """
        if player.number == 1:
            current_area = P1_PITS
        else:
            current_area = P2_PITS

        # Pick up the stones from the right pit.
        stones_grabbed = self.board[current_area][start_index]
        self.board[current_area][start_index] = 0

        # Ready a moving index
        index = start_index

        for stone in range(stones_grabbed):
            try:
                # Try to place in adjacent pit prior to incrementing index.
                self.board[current_area][index+1] += 1
                # Stone successfully placed, so increase index.
                index += 1
            except IndexError:
                # Proceed to next area
                current_area = self.get_next_area(current_area)

                # Check to ensure opposing store is skipped.
                if player.number == 1 and current_area == P2_STORE:
                    current_area = self.get_next_area(current_area)
                elif player.number == 2 and current_area == P1_STORE:
                    current_area = self.get_next_area(current_area)
                else:
                    pass
                # Reset index and increment stone at current position
                index = 0
                self.board[current_area][index] += 1

        return self.board

    def get_next_area(self, current_area):
        """ Given a current area of transaction, gives the next area. """
        if current_area == P1_PITS:
            return P1_STORE
        elif current_area == P1_STORE:
            return P2_PITS
        elif current_area == P2_PITS:
            return P2_STORE
        elif current_area == P2_STORE:
            return P1_PITS
        else:
            raise InvalidBoardArea

    def get_player1_score(self):
        """ Returns score for Player 1. """
        return self.board[1][0]

    def get_player2_score(self):
        """ Returns score for Player 2"""
        return self.board[3][0]
