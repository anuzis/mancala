""" Tests for Mancala board functions. """

import unittest

from ..mancala.board import Board, InvalidMove
from ..mancala.constants import P1_PITS, P2_PITS, P1_STORE, P2_STORE

class TestPlayer1Moves(unittest.TestCase):
    """ Tests for Mancala Board functions. """

    def setUp(self):
        """ Prepare test boards for Player 1. """
        # First three boards test player1 from starting position.
        self.board1 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])

        self.board2 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])

        self.board3 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])

        # Board 4 tests a loop back to player one's pits.
        self.board4 = Board(test_state=[[4, 4, 4, 4, 10, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])

        # Board 5 tests player 1 capturing stones from player 2
        self.board5 = Board(test_state=[[5, 4, 4, 4, 4, 0], [1], \
            [5, 5, 0, 5, 5, 5], [1]])

    def test_player1__move_stones(self):
        """ Tests that _move_stones works as expected.

        Takes a Board instance as input. """

        # Test from own pits to own pits
        assert self.board1._move_stones(1, 1)[0] == \
                            [[4, 0, 5, 5, 5, 5], [0], \
                            [4, 4, 4, 4, 4, 4], [0]]
        # Test from own pits to own store
        assert self.board2._move_stones(1, 2)[0] == \
                            [[4, 4, 0, 5, 5, 5], [1], \
                            [4, 4, 4, 4, 4, 4], [0]]
        # Test from own pits to an opposing pit
        assert self.board3._move_stones(1, 3)[0] == \
                            [[4, 4, 4, 0, 5, 5], [1], \
                            [5, 4, 4, 4, 4, 4], [0]]

        # Test from own pits back through to own pits, skipping opp store
        assert self.board4._move_stones(1, 4)[0] == \
                            [[5, 5, 4, 4, 0, 5], [1], \
                            [5, 5, 5, 5, 5, 5], [0]]

        print "test_player1__move_stones() tests pass."

    def test_free_move_earned(self):
        """ Test that free moves are only earned in one's own store. """
        assert self.board2._earned_free_move(1, P1_STORE)
        assert self.board5._earned_free_move(2, P2_STORE)
        self.assertFalse(self.board2._earned_free_move(1, P1_PITS))
        self.assertFalse(self.board2._earned_free_move(1, P2_PITS))
        self.assertFalse(self.board2._earned_free_move(2, P2_PITS))

    def test_player1_stone_capture(self):
        """ Test player 1 capturing stones from player 2 """
        self.assertEqual(self.board5._move_stones(1, 1)[0],
                            [[5, 0, 5, 5, 5, 0], [7],
                            [0, 5, 0, 5, 5, 5], [1]])

        print "test_player1_stone_capture() tests pass."

    def test_get_score(self):
        """ Test that Board.get_score works while we have boards ready. """
        self.board3._move_stones(1, 3)
        self.assertEqual(self.board3.get_score(1), 1)
        self.assertEqual(self.board3.get_score(2), 0)
        self.board5.board = self.board5._move_stones(1, 1)[0]
        print "Board 5: " + str(self.board5.board)
        self.assertEqual(self.board5.get_score(1), 7)
        self.assertEqual(self.board5.get_score(2), 1)

    def test_get_scores(self):
        """ Test that get_scores works. """
        self.board5._move_stones(1, 1)
        self.assertEqual(self.board5.get_scores(), (7, 1))

    def test_invalid_move(self):
        """ Confirm InvalidMove raised when no stones at given index. """
        with self.assertRaises(InvalidMove):
            self.board5._move_stones(1, 5)

    def test_reverse_index(self):
        """ Test that _reverse_index works. """
        # Assumes 6 pits.
        from ..mancala.mancala import reverse_index
        self.assertEqual(reverse_index(0), 5)
        self.assertEqual(reverse_index(1), 4)
        self.assertEqual(reverse_index(2), 3)
        self.assertEqual(reverse_index(3), 2)
        self.assertEqual(reverse_index(4), 1)
        self.assertEqual(reverse_index(5), 0)

    def test_get_opposing_area_and_index(self):
        """ Test that _get_opposing_area_and_index works. """
        self.assertEqual((P1_PITS, 5), self.board5._get_opposing_area_and_index(P2_PITS, 0))
        self.assertEqual((P2_PITS, 5), self.board5._get_opposing_area_and_index(P1_PITS, 0))
        self.assertEqual((P1_PITS, 2), self.board5._get_opposing_area_and_index(P2_PITS, 3))
        self.assertEqual((P2_PITS, 3), self.board5._get_opposing_area_and_index(P1_PITS, 2))

class TestPlayer2Moves(unittest.TestCase):
    """ Tests for Mancala Board functions. """

    def setUp(self):
        """ Prepare test boards for player 2. """

    	# Board 5 tests player 2 moving to opposing player's pits.
        self.board1 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])

    	# Board 6 tests player 2 looping back to his own pits.
        self.board2 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 15, 4, 4, 4], [0]])

    def test_player2__move_stones(self):
        """ Tests that _move_stones works as expected. """

        # Test player 2 movement to opposing pit
        assert self.board1._move_stones(2, 5)[0] == \
                            [[5, 5, 5, 4, 4, 4], [0], \
                            [4, 4, 4, 4, 4, 0], [1]]
        # Test player 2 movement through to own pits, skipping opp store,
        # returning through starting pit, and proceeding further
        assert self.board2._move_stones(2, 2)[0] == \
                            [[5, 5, 5, 5, 5, 5], [0], \
                            [5, 5, 1, 6, 6, 5], [1]]

        print "test_player2__move_stones() tests pass."

class TestTextifyBoardFunctions(unittest.TestCase):
    """ Tests for Mancala Board functions. """

    def setUp(self):
        """ Setup a board to textify. """
        self.board = Board(test_state=[[4, 4, 4, 0, 5, 5], [1], \
                            [5, 4, 4, 4, 4, 4], [0]])

    def test_textify_board(self):
        """ Test that textify_board correctly renders board.
        Takes a Board instance as input. """
        assert self.board.textify_board() == \
                                    "   4  4  4  4  4  5\n 0                    1\n   4  4  4  0  5  5\n"
        print "textify_board() tests pass."
