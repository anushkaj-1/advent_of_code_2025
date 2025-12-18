import pandas as pd

'''
This file contains the solution for day 1 of Advent of Code. 
There is a lock guarding the North Pole, it is a circular lock with incremental ticks from 0-99.
The given input file "day1input.txt" contains a series of turns on the lock to get the new password.
The password is the number of times the pointer lands on 0 throughout these turns
'''
# Dial starts at 50
turns = []

with open("day1input.txt", "r") as file:
    for line in file:
        turns.append(line)


#def lockPassword(turns: Array<string>) -> Integer:
    dialPosition = 50
    zeroCount = 0
