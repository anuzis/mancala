""" Main script to begin playing a match of Mancala. """
from mancala.mancala import Match, HumanPlayer
from mancala.ai_profiles import VectorAI

def main():
    """ Script to begin a match of Mancala. """
    print("Welcome to Mancala!")
    match = Match(player1_type=HumanPlayer, player2_type=VectorAI)
    match.handle_next_move()

if __name__ == '__main__':
    main()
