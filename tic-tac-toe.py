

# thank you Al, http://inventwithpython.com/chapter10.html

import random

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

def inputPlayerLetter():
	# Lets the player type which letter they want to be
	# Returns a list with the player's letter as the first item, and the computer's letter as the second.
	letter = ""
	while not (letter == 'X') or (letter == 'O'):
		print('Do you want to be X or O?')
		letter = input().upper()

	#The first element in the list is the player's letter, the second is the computer's latter
	if letter == 'X':
		# player's letter = X, computer's = O
		return ['X', 'O']
	else:
		# player's letter = O, computer's = X
		return['O','X']

def whoGoesFirst():
	# Randomly choose the player who goes first.
	if random.randint(0,1) == 0:
		return 'computer'
	else:
		return 'player'
		
# just trying to get python IDE working in sublime
print("kdfgkldfgklfdkfdlklkgdf")