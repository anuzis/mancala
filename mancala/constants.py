""" Mancala constants file. """

# Constants, reflective of index within board
P1_PITS = 0
P1_STORE = 1
P2_PITS = 2
P2_STORE = 3
REVERSE_INDEX = 5 # Functions assuming there are 6 pits indexed 0 to 5

# Player names
DEFAULT_NAME = 'Player'
AI_NAME = 'AI'

# Player types
HUMAN_PLAYER = 0
AI_PLAYER = 1
DEFAULT_TYPE = HUMAN_PLAYER

# AI Profiles
RANDOM_AI = 0 # purely random
VECTOR_AI = 1 # optimizes for free turns only considering own side
DEFAULT_AI = 1
