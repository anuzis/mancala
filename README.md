NOTE: Game is not functional yet. Started developing yesterday, it still has a ways to go.

First attempt at an object oriented implementation of Mancala, purely for my own learning.

Not planning on a fancy UI (using print statements in Python).

Looking forward to developing a variety of AI profiles to play against.


### Design notes

## Concept inventory
# TDD!
# Cyclical board with pits, stones, stores
# Players who take turns
# Stone transactions: moving, capturing
# Free turn
# Display UI
# Accept user input for turn.

## Needed AI support functions
# def captures_stones - AI checks if an option captures stones
# def gets_another_turn - AI checks if an option gets another turn
# def finishes_game - AI checks if an option finishes the game
# def calculate_second_finisher_score - AI calculates score of 2nd finisher

## AI Profile Ideas
# Random: selects move at random
# FreeMove: optimizes for free moves.
# Capture: optimizes for capture.
# DecisionTree Deterministic: follows a mixed-strategy decision tree
# DecisionTree Stochastic: varies selection between top Decision Tree options
# MonteCarlo: searches for best move via Monte Carlo simulation

## AI Decision Tree Ideas
# Check if any moves capture stones (calculate value Vs free moves)
# Check for sequences to maximize free turns
# Check for sequences that maximize free turns AND capture
# Else: go with moves that line up another turn on next turn
# Check future state: if taking a certain interaction sets up good next turn
# Check other player ability to disrupt: if taking interaction allows other player to disrupt
# Test various probabilities to each selection