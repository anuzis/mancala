""" Module for Mancala AI Profiles. """

from random import choice

from mancala.mancala import Player, reverse_index
from mancala.constants import AI_NAME, P1_PITS, P2_PITS

class AIPlayer(Player):
    """ Base class for an AI Player """
    def __init__(self, number, board, name=AI_NAME):
        """ Initializes an AI profile. """
        super(AIPlayer, self).__init__(number, board, name)

    @property
    def pits(self):
        """ Shortcut to AI pits. """
        if self.number == 1:
            return self.board.board[P1_PITS]
        else:
            return self.board.board[P2_PITS]

    @property
    def eligible_moves(self):
        """ Returns a list of integers representing eligible moves. """
        eligible_moves = []
        for i in range(len(self.pits)):
            if not self.pits[i] == 0:
                eligible_moves.append(i)
        return eligible_moves

    @property
    def eligible_free_turns(self):
        """ Returns a list of indexes representing eligible free turns. """

        free_turn_indices = range(6, 0, -1)

        elig_free_turns = []

        for i in range(0, 6):
            if self.pits[i] == free_turn_indices[i]:
                elig_free_turns.append(1)
            else:
                elig_free_turns.append(0)

        return elig_free_turns

    def _think(self):
        """ Slight delay for thinking. """
        import time
        print("AI is thinking...")
        time.sleep(3)

class RandomAI(AIPlayer):
    """ AI Profile that randomly selects from eligible moves. """

    def get_next_move(self):
        """ Returns next AI move based on profile. """

        self._think()

        return choice(self.eligible_moves)

class VectorAI(AIPlayer):
    """ AI Profile using a simple vector decision method. """

    def get_next_move(self):
        """ Use an reverse indices vector to optimize for free turns. """

        self._think()

        reverse_indices = range(5, -1, -1)

        # First optimize for free moves.
        for i in reverse_indices:
            if self.eligible_free_turns[i] == 1:
                if self.pits[i] == reverse_index(i) + 1:
                    print("VectorAI, mode 1, playing: ", str(i))
                    return i
        # Then clear out inefficient pits.
        for i in reverse_indices:
            if self.pits[i] > reverse_index(i) + 1:
                print("VectorAI, mode 2, playing: ", str(i))
                return i
        # Finally, select a random eligible move.
        print("VectorAI, mode 3, playing an eligible move.")
        return choice(self.eligible_moves)
