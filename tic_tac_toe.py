"""
@author Garrett Starkey
@version 1

Allows a user to play a complete game of TicTacToe. 

"""

	
# creating a board
board = [["_" for _ in range(3)] for _ in range(3)]
         
# printing the board to the console
def printBoard(board):
	[print(row) for row in board]	
printBoard(board)

# logic behind the game, placing the X or O on the board
def game():
	turn = 'X'
	count = 0

	for i in range(10):
		printBoard(board)
		print("It's your turn " + turn + ", where would you like to place?")

		move = int(input())

		if board[move] == ' ':
 			board[move] = turn
		else:
			print("That spot is already taken.\nTry again")
game() 	

	#TODO determine a winner

	#TODO print a winning message	
