""" Tests for Mancala MatchMaker functions. """

import unittest

from ..mancala.mancala import Board, Player, MatchMaker

class TestBoardFunctions(unittest.TestCase):
    """ Tests for MatchMaker functions. """

    def setUp(self):
    	self.matchmaker = MatchMaker()
    	self.player1 = Player(1)
    	self.player2 = Player(2)
    	self.board = Board()
