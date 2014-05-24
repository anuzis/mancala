""" Mancala tests module. """

import unittest

class TestBoardFunctions(unittest.TestCase):
    """ Tests for Mancala Board functions. """

    def setUp(self):
    	self.player1 = Player(1)
    	self.player2 = Player(2)

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

    	# Board 5 tests player 2 moving to opposing player's pits.
    	self.board5 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])

    	# Board 6 tests player 2 looping back to his own pits.
    	self.board6 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 15, 4, 4, 4], [0]])


    def test_move_stones():
        """ Tests that move_stones works as expected.

        Takes a Board instance as input. """

        # Test from own pits to own pits
        assert self.board1.move_stones(self.player1, 1) == \
                            [[4, 0, 5, 5, 5, 5], [0], \
                            [4, 4, 4, 4, 4, 4], [0]]
        # Test from own pits to own store
        assert self.board2.move_stones(self.player1, 2) == \
                            [[4, 4, 0, 5, 5, 5], [1], \
                            [4, 4, 4, 4, 4, 4], [0]]
        # Test from own pits to an opposing pit
        assert self.board3.move_stones(self.player1, 3) == \
                            [[4, 4, 4, 0, 5, 5], [1], \
                            [5, 4, 4, 4, 4, 4], [0]]
        # Test from own pits back through to own pits, skipping opp store
        assert self.board4.move_stones(self.player1, 4) == \
                            [[5, 5, 4, 4, 0, 5], [1], \
                            [5, 5, 5, 5, 5, 5], [0]]
        # Test player 2 movement to opposing pit
        assert self.board5.move_stones(self.player2, 5) == \
                            [[5, 5, 5, 4, 4, 4], [0], \
                            [4, 4, 4, 4, 4, 0], [1]]
        # Test player 2 movement through to own pits, skipping opp store,
        # returning through starting pit, and proceeding further
        assert self.board6.move_stones(self.player2, 2) == \
                            [[5, 5, 5, 5, 5, 5], [0], \
                            [5, 5, 1, 6, 6, 5], [1]]

        print "move_stones() tests pass."


    def test_textify_board():
        """ Test that textify_board correctly renders board.
        Takes a Board instance as input. """
        self.board = Board(test_state=[[4, 4, 4, 0, 5, 5], [1],
                                    [5, 4, 4, 4, 4, 4], [0]])
        assert self.board.textify_board() == \
                                    "   4  4  4  4  4  5\n 0                    1\n   4  4  4  0  5  5\n"
        print "textify_board() tests pass."