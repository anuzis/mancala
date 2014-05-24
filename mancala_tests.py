""" Mancala tests module. """

from .constants import *
from .mancala import AIProfile, Board, InvalidBoardArea, Player

def mancala_tests():
    """ Tests for Mancala

    TODO(anuzis): This should probably be a Class, not a method. """

    player1 = Player(1)
    player2 = Player(2)

    def test_move_stones():
        """ Tests that move_stones works as expected.

        Takes a Board instance as input. """

        # Test from own pits to own pits
        board1 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])

        assert board1.move_stones(player1, 1) == \
                            [[4, 0, 5, 5, 5, 5], [0], \
                            [4, 4, 4, 4, 4, 4], [0]]
        # Test from own pits to own store
        board2 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])
        assert board2.move_stones(player1, 2) == \
                            [[4, 4, 0, 5, 5, 5], [1], \
                            [4, 4, 4, 4, 4, 4], [0]]
        # Test from own pits to an opposing pit
        board3 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])
        assert board3.move_stones(player1, 3) == \
                            [[4, 4, 4, 0, 5, 5], [1], \
                            [5, 4, 4, 4, 4, 4], [0]]
        # Test from own pits back through to own pits, skipping opp store
        board4 = Board(test_state=[[4, 4, 4, 4, 10, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])
        assert board4.move_stones(player1, 4) == \
                            [[5, 5, 4, 4, 0, 5], [1], \
                            [5, 5, 5, 5, 5, 5], [0]]
        # Test player 2 movement to opposing pit
        board5 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 4, 4, 4, 4], [0]])
        assert board5.move_stones(player2, 5) == \
                            [[5, 5, 5, 4, 4, 4], [0], \
                            [4, 4, 4, 4, 4, 0], [1]]
        # Test player 2 movement through to own pits, skipping opp store,
        # returning through starting pit, and proceeding further
        board6 = Board(test_state=[[4, 4, 4, 4, 4, 4], [0], \
            [4, 4, 15, 4, 4, 4], [0]])
        assert board6.move_stones(player2, 2) == \
                            [[5, 5, 5, 5, 5, 5], [0], \
                            [5, 5, 1, 6, 6, 5], [1]]

        print "move_stones() tests pass."


    def test_textify_board():
        """ Test that textify_board correctly renders board.
        Takes a Board instance as input. """
        board = Board(test_state=[[4, 4, 4, 0, 5, 5], [1],
                                    [5, 4, 4, 4, 4, 4], [0]])
        assert board.textify_board() == \
                                    "   4  4  4  4  4  5\n 0                    1\n   4  4  4  0  5  5\n"
        print "textify_board() tests pass."