
# SublimeREPL: Python run current file
# a = raw_input("test raw input")

import random

# thank you Al, http://inventwithpython.com/chapter10.html
def drawBoard(board):
	# function prints out the board that it was passed
	# 'board' is a list of 10 strings representing the board (ignore index 0)
	print('   |   |')
	print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
	print('   |   |')
	print('-----------')
	print('   |   |')
	print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
	print('   |   |')

def whoGoesFirst():
	# Randomly choose the player who goes first.
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'

def makeMove(board, letter, move):
	board[move] = letter

def isWinner(bo, le):
	# Given a board and a player's letter, this function returns True if that player has won.
	#we use bo instead of board and le instead of letter so we don't have to type
	return ((bo[7] == le and bo[8] == le and bo[9] == le) or # across the top
	(bo[4] == le and bo[5] == le and bo[6] == le) or # across the middle
	(bo[1] == le and bo[2] == le and bo[3] == le) or # across the bottom
	(bo[7] == le and bo[4] == le and bo[1] == le) or # down the left side
	(bo[8] == le and bo[5] == le and bo[2] == le) or # down the middle
	(bo[9] == le and bo[6] == le and bo[3] == le) or # down the right side
	(bo[7] == le and bo[5] == le and bo[3] == le) or # diagonal
	(bo[9] == le and bo[5] == le and bo[1] == le)) # diagonal

def getBoardCopy(board):
	# Make a duplicate of the board list and return it as a duplicate.
	dupeBoard = []

	for i in board:
		dupeBoard.append(i)

	return dupeBoard

def isSpaceFree(board, move):
	#Return true if the passed move is free on the board.
	return board[move] == ''

move = ''	
def getPlayerMove(board):
	#player's move is random
	move = ''
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
		print('What is your next move? (1-9)')
		# move = input()
		# screw letting the player choose, randomize it!
		move = random.randint(0,9)
	return int(move)

#print test code
turn = whoGoesFirst()
theBoard = [' '] * 10

#drawBoard(theBoard)
print turn + " goes first"