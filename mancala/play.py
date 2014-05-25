""" Main script to begin playing a match of Mancala. """

if __name__ == '__main__' and __package__ is None:
    from os import sys, path
    sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from .mancala import Match, HumanPlayer, AIPlayer

def main():
    """ Script to begin a match of Mancala. """
    print "Welcome to Mancala!"
    match = Match(player1_type=HumanPlayer, player2_type=AIPlayer)
    match.handle_next_move()

if __name__ == '__main__':
    main()
