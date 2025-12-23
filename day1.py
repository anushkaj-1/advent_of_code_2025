import pandas as pd

'''
This file contains the solution for day 1 of Advent of Code. 
There is a lock guarding the North Pole, it is a circular lock with incremental ticks from 0-99.
The given input file "day1input.txt" contains a series of turns on the lock to get the new password.
The password is the number of times the pointer lands on 0 throughout these turns
'''
# Dial starts at 50

with open("day1input.txt", "r") as file:
    turns = [line for line in file]

"""
Helper function: splits up a turn into a direction and magnitude
Args: string representing a single turn within a series of turns
Returns: List[string, int] with position [0] being direction and position [1] being magnitude
"""
def splitTurn(turn):
    direction = turn[0]
    magnitude = turn[1:]
    magnitude = int(magnitude)
    splitturn = [direction, magnitude]
    return splitturn


"""
Determines the number of times a lock combination lands on 0
Args: array (strings) representing the direction and number of tick marks to turn
Returns: int representing the number of times in the lock combination that 0 is reached
"""
def lockPassword(turns):
    # initial dial position
    dialPosition = 50
    zeroCount = 0
    for turn in turns:
        lastPosition = dialPosition
        splitturn = splitTurn(turn)
        if splitturn[0] == "R":
            dialPosition += splitturn[1]
            if dialPosition > 99:
                dialPosition -= 99
        elif splitturn[0] == "L":
            dialPosition -= splitturn[1]
            if dialPosition < 0:
                toTurnFromEnd = splitturn[1] - (lastPosition + 1)
                dialPosition = 99 - toTurnFromEnd
        if dialPosition == 0:
            zeroCount += 1
    return zeroCount


