#Class: Creates players of the game

"""
Author: Gilbert Adu
Started: 5th July 2019 7:56 am
Date Finished: 5th July 2019, 8:06 am



The file players.py contains a class which makes players of the game.
The idea is to turn a person(their name) into a recognized game player.
"""

class Player():



    def __init__(self,name=None):

        self.name = name
        self.started = 0
        self.wins = 0
