""" Main script to begin playing a match of Mancala. """

from .mancala import Match

def main():
    """ Script to begin a match of Mancala. """
    print "Welcome to Mancala!"
    match = Match()
    match.handle_next_move()

if __name__ == '__main__':
    main()
