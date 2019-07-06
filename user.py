"""
Author: Gilbert Adu
Started: 5th July 2019 7:56 am
Date Finished: 5th July 2019, 8:06 am


"""

"""
This is the user interface.
This is what should be run from the terminal

Users should input their names so they can be turned into players
Users should see the hidden word and its progress,and guesses left

"""


import players
import  backend

first = input("Please enter name for first player: " )
second = input("Please enter name for second player: " )

my_first = players.Player(first)
my_second = players.Player(second)

backend.thegame(my_first,my_second)
