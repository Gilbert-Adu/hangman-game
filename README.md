# hangman-game
this is my version of the popular hangman game

#players.py
The file players.py contains a class which makes players of the game.
The idea is to turn a person(their name) into a recognized game player.

#user.py
This is the user interface.
This is what should be run from the terminal

Users should input their names so they can be turned into players
Users should see the hidden word and its progress,and guesses left

#backend.py

Contains the chunk of the code and is the backend of the game.

UNDERSTANDING THE CODE:

1. The function thegame() accepts two players at a time

2.It asks the first player to give a word, presents only the first and last
characters of the word, and asks player2 to guess the missing letters.

3.It keeps track of the number of times a particular player starts the game(the
number of times a player presents a word to be guessed.)

4. If at any point, the number of times player1 starts is greater than the times
player2 starts, then it calls itself recursively with player2 as player1 and vice
versa. If player2's starts is greater than that of player1, it recurses again

5. When the number of starts of both players becomes equal, it checks and compares
the number of wins of the players and announces the one with the higher wins
as the winner.

