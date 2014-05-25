""" Tests for Mancala Match functions. """

import unittest

from ..mancala.mancala import Match

class TestMatchFunctions(unittest.TestCase):
    """ Tests for Match functions. """

    def setUp(self):
        self.match = Match()

    def test_player_numbers_assigned(self):
        """ Test that player numbers are properly assigned """
        assert self.match.player1.number == 1
        assert self.match.player2.number == 2

    def test_turn_swap(self):
        """ Test that it starts as player1's turn and swaps correctly. """
        assert self.match.current_turn == self.match.player1
        assert self.match._swap_current_turn() == self.match.player2
        assert self.match._swap_current_turn() == self.match.player1

    def test_player1_win(self):
        """ Test that a won match is detected. """
        self.match.board.board = [[0, 0, 0, 0, 0, 3], [0], [4, 4, 4, 4, 4, 4], [0]]
        self.match.board._move_stones(1, 5)
        self.assertEqual(self.match._check_for_winner(), True)

    def test_player2_win(self):
        """ Test that a won match is detected. """
        self.match.board.board = [[4, 4, 4, 4, 4, 4], [0], [0, 0, 0, 0, 0, 3], [0]]
        self.match.board._move_stones(2, 5)
        self.assertEqual(self.match._check_for_winner(), True)
