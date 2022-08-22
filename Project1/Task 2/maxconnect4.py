#!/usr/bin/env python

# Written by Chris Conly based on C++
# code provided by Dr. Vassilis Athitsos
# Written to be Python 2.4 compatible for omega


#CSE 5360 - Artificial Intelligence
#Project 1 - Task 2
#Modified by
#Student Name: Sujitraj Thirumurthy 
#Student Id: 1001830297

#Written in Python (Version 3.8.9)

import sys
from MaxConnect4Game import *

def oneMoveGame(currentGame):
    if currentGame.pieceCount == 42:    # Is the board full already?
        print ('BOARD FULL\n\nGame Over!\n')
        sys.exit(0)

    currentGame.aiPlay() # Make a move (only random is implemented)

    print ('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()


def interactiveGame(currentGame,nextPlayer):
    # printing current board game 
    print("Printing the current Game Board")
    currentGame.printGameBoard()
    # checking if the next player is human or AI 
    if nextPlayer == 'human-next':
        #Human Turn 
        playerHuman(currentGame)
        # currentGame(playerHuman)
    else:
        #computer Turn
        computerPlayer(currentGame)
        playerHuman(currentGame) #human turn next
    # Displaying the Final Result of the Game 
    displayFinalResult(currentGame)

    

    # sys.exit('Interactive mode is currently not implemented')
def computerPlayer(currentGame):
        currentGame.aiPlay()  
        currentGame.gameFile = open('computer.txt', 'w')  
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()  
        currentGame.printGameBoard()   
        currentGame.countScore()  
        print(' PlayerA Score  = %d, PlayerB Score = %d\n' % (currentGame.player1Score, currentGame.player2Score))
        # playerHuman(currentGame)    # human turn next

def playerHuman(currentGame):
    while currentGame.pieceCount != 42:
        print('Human Player Turn to Play ')
        playerMove = int(input("Enter a Column from 1 to 7 "))
        print('Player Move Displayed',str(playerMove))
        currentGame.printGameBoard()
        # writting the move into the file 
        currentGame.gameFile = open("human.txt",'w')
        currentGame.printGameBoardToFile()
        currentGame.gameFile.close()
        if currentGame.pieceCount == 42:
            displayFinalResult(currentGame)
        else:
            computerPlayer(currentGame)


def displayFinalResult(currentGame):
    #checking if gameBoard is Full 
    if currentGame.pieceCount == 42 :
        if currentGame.player1Score > currentGame.player2Score:
            print("player 1 Wins the Game")
        elif currentGame.player1Score == currentGame.player2Score:
            print('Game Ends in a Tie')
        else:
            print('Player2 Wins the game')
        print('Game Over')

    

def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print ('\nMaxConnect-4 game\n')
    print ('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    if game_mode == 'interactive':
        interactiveGame(currentGame,argv[3].lower()) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)



