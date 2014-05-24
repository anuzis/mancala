First attempt at an object oriented program, purely for my own learning. Once working, the program should allow you to play Mancala against a variety of AI profiles.

Not planning on a fancy UI (using print statements in Python).

## Design notes (mostly for my own reference)

### Concept inventory
TDD!
Cyclical board with pits, stones, stores
Players who take turns
Stone transactions: moving, capturing
Free turn
Display UI
Accept user input for turn.

### Needed AI support functions
captures_stones - AI checks if an option captures stones
gets_another_turn - AI checks if an option gets another turn
finishes_game - AI checks if an option finishes the game
calculate_second_finisher_score - AI calculates score of 2nd finisher

### AI Profile Ideas
Random: selects move at random
FreeMove: optimizes for free moves.
Capture: optimizes for capture.
DecisionTree Deterministic: follows a mixed-strategy decision tree
DecisionTree Stochastic: varies selection between top Decision Tree options
MonteCarlo: searches for best move via Monte Carlo simulation

### AI Decision Tree Ideas
Check if any moves capture stones (calculate value Vs free moves)
Check for sequences to maximize free immediate turns
Check for sequences that maximize free turns AND capture
Check future state: if taking a certain interaction sets up good next turn
Check other player ability to disrupt: if taking interaction allows other player to disrupt
Else: evaluate moves that optimize free turn potential
Test various probabilities to each selection