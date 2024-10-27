""" Module for Mancala Board class. """

from mancala.constants import P1_PITS, P1_STORE, P2_PITS, P2_STORE, REVERSE_INDEX

class InvalidBoardArea(Exception):
    """ Exception flagged when moves are attempted on an unknown area. """
    pass

class InvalidMove(Exception):
    """ Exception flagged when no stones are available at given index. """
    pass

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

    def _move_stones(self, player_num, start_index):
        """ Moves stones by the Player associated with player_num,
        starting at the given index.

        Returns: new state of Board.board, earned_free_move (bool)

        player_num: integer from Player.number class
        start_index: integer specified by player (must be 0-5)
        """
        if player_num == 1:
            current_area = P1_PITS
        else:
            current_area = P2_PITS

        # Confirm stones are available at the given index.
        if not self.board[current_area][start_index]:
            raise InvalidMove

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
                current_area = self._get_next_area(current_area)

                # Check to ensure opposing store is skipped.
                if player_num == 1 and current_area == P2_STORE:
                    current_area = self._get_next_area(current_area)
                elif player_num == 2 and current_area == P1_STORE:
                    current_area = self._get_next_area(current_area)
                else:
                    pass
                # Reset index and increment stone at current position
                index = 0
                self.board[current_area][index] += 1

        if self._earned_free_move(player_num, current_area):
            earned_free_move = True
        else:
            earned_free_move = False

        # If last move earned a capture, process it.
        if self._earned_capture(player_num, current_area, index):
            self.board = self._process_capture(current_area, index)

        return self.board, earned_free_move

    def _earned_free_move(self, player_num, last_area):
        """ Checks whether a free move was earned. """
        if player_num == 1 and last_area == P1_STORE:
            print("Earned free move!")
            return True
        elif player_num == 2 and last_area == P2_STORE:
            print("Earned free move!")
            return True
        else:
            return False

    def _earned_capture(self, player_num, last_area, last_index):
        """ Checks whether the last move earned a capture.

        last_area: integer associated with last board area
        last_index: integer of the last move's index
        """

        opposing_area, opposing_index = self._get_opposing_area_and_index(
            last_area, last_index)

        # Check whether last move was in Player's own pits.
        if player_num == 1:
            if not last_area == P1_PITS:
                return False
        elif player_num == 2:
            if not last_area == P2_PITS:
                return False
        else:
            pass

        # Check whether last move's pit now has more than 1 stone.
        if self.board[last_area][last_index] > 1:
            return False

        # Check whether opposite pit has capturable stones.
        elif self.board[opposing_area][opposing_index] == 0:
            return False

        # Placed stone in own empty pit, adjacent capturable stones.
        else:
            return True

    def _process_capture(self, last_area, last_index):
        """ Processes capture by moving stones to the player's store. """

        if last_area == P1_PITS:
            destination_store = P1_STORE
        else:
            destination_store = P2_STORE

        opposing_area, opposing_index = self._get_opposing_area_and_index(
            last_area, last_index)

        captured_stones = self.board[opposing_area][opposing_index]
        print("%d stones captured!" % captured_stones)

        # Clear the two pits
        self.board[last_area][last_index] = 0
        self.board[opposing_area][opposing_index] = 0

        # Move captures and original stone to store
        total_gain = captured_stones + 1
        self.board[destination_store][0] += total_gain

        return self.board

    def gather_remaining(self, player_num):
        """ Gathers stones from remaining_area and deposits
        in the associated player's store. (when game is finished)

        Returns finished Board.board state."""
        
        if player_num == 1:
            remaining_area = P1_PITS
            destination_store = P1_STORE
        elif player_num == 2:
            remaining_area = P2_PITS
            destination_store = P2_STORE
        else:
            raise Exception("Unknown player.")

        remaining_stones = 0
        for i in range(6):
            remaining_stones += self.board[remaining_area][i]
            self.board[remaining_area][i] = 0

        self.board[destination_store][0] += remaining_stones

        return self.board

    def _get_opposing_area_and_index(self, orig_area, index):
        """ Returns opposing_area, opposing_index

        Optionally returns as tuple for assertion testing.
         """

        if orig_area == P1_PITS:
            opposing_area = P2_PITS
        elif orig_area == P2_PITS:
            opposing_area = P1_PITS
        elif orig_area == P1_STORE:
            opposing_area = P2_STORE
        elif orig_area == P2_STORE:
            opposing_area = P1_STORE
        else:
            raise InvalidBoardArea

        opposing_index = REVERSE_INDEX-index

        return opposing_area, opposing_index


    def _get_next_area(self, current_area):
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

    def get_score(self, player_num):
        """ Returns score for player_num. """
        if player_num == 1:
            return self.board[1][0]
        else:
            return self.board[3][0]

    def get_scores(self):
        """ Returns both scores as a tuple. """
        return (self.board[1][0], self.board[3][0])