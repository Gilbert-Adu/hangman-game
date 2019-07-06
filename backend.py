"""
Author: Gilbert Adu
Started: 5th July 2019 7:56 am
Date Finished: 6th July 2019, 11:32 am
"""


"""
Contains the chunk of the code and is the backend of the game.

###UNDERSTANDING THE CODE:

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
"""

import players


def thegame(player1,player2):


    NUM_GAMES_PLAYED = 0
    while NUM_GAMES_PLAYED <= 3:
        i = 0
        t = 1

        word = input( player1.name+", please choose a word: ")
        j = len(word)-1
        k = j

        hidden=''
        guesses_left = len(word)
        for letter in range(len(word)):
            hidden = hidden + '_'
        hidden = list(hidden)
        hidden[i],hidden[j] = word[i],word[j]
        hidden="".join(hidden)

        print("The hidden word is "+hidden)


        response = list(hidden)
        while t < k:
            guessed = input(player2.name+', please guess the next letter of the word: ')
            response[t] = guessed
            t += 1
        response = "".join(response)
        print("The correct word is " + word)

        player1.started += 1

        if word == response:
            player2.wins += 1
            print("CONGRATULATIONS! "+player2.name+" YOU WON THIS ROUND")
        elif word != response:
            player1.wins += 1
            print("CONGRATULATIONS! "+player1.name+" YOU WON THIS ROUND")

        if player1.started == 3 and player2.started == 3:
            if player1.wins > player2.wins:

                print("GAMEOVER!!!")
                print(player1.name+" is the WINNER")

            else:
                print("GAMEOVER!!!")
                print(player2.name+" is the WINNER")






        if player2.started < player1.started:
            thegame(player2,player1)


        elif player1.started < player2.started:
            thegame(player1,player2)
