"""
@author Garrett Starkey
@version 1

Allows a user to play a complete game of TicTacToe. 

"""

class TicTacToe:
	
	# creating a board
	board = [["_" for _ in range(3)] for _ in range(3)]

	# prints a board to the console, utilizing list comprehension
	def print_board(board):
		[print(row) for row in board]	
	print_board(board)
		

	#TODO determine whose turn it is

	#TODO determine a winner

	#TODO print a winning message	
