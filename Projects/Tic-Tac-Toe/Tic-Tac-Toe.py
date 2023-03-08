"""
Tic-Tac-Toe finished
"""

def printBoard(board):
	print(f" {board[0]} | {board[1]} | {board[2]}")
	print("-----------") #11 dashes
	print(f" {board[3]} | {board[4]} | {board[5]}")
	print("-----------") #11 dashes
	print(f" {board[6]} | {board[7]} | {board[8]}")

def findWinner(board):
	#Horizantal winning conditions first
	if board[0] == board[1] == board[2]:
		return board[0]
	elif board[3] == board[4] == board[5]:
		return board[3]
	elif board[6] == board[7] == board[8]:
		return board[6]
	#Verticle columns 
	elif board[0] == board[3] == board[6]:
		return board[0]
	elif board[1] == board[4] == board[7]:
		return board[1]
	elif board[2] == board[5] == board[8]:
		return board[2]
	#Diagonals
	elif board[0] == board[4] == board[8]:
		return board[0]
	elif board[2] == board[4] == board[6]:
		return board[2]
	#In case there's no winner yet
	else:
		return False

def placeXO(board):
	
	print("Who's turn is it? X or O?")
	player = input() #Enter X or O

	#Remember the NOT logical operator
	#if the player is NOT ("x" or "o") -> do something
	if not (player == "x" or player == "o"): 
		print("Please enter x or o")
		return False #Error

	print("Which tile do you want to choose?")
	tile_number = int(input()) #0-8

	#Remember your less than or equal to signs. This is valid in python
	if not (0 <= tile_number <= 8):
		print("Please enter a number between 0-8")
		return False

	#Check if it already has x or o in it. 
	if board[tile_number] == "x" or board[tile_number] == "o":
		print("Please choose an empty tile")
		return False

	print("Placing", player, "on tile number", tile_number)
	board[tile_number] = player

	return board

def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

	turns = 1
	while True: #The game loop
		printBoard(board)
		
		if turns > 9:
			print("Tie")
			return

		winner = findWinner(board)
		if winner != False:
			print("The winner is: ", winner)
			return

		temp_board = placeXO(board)
		if temp_board == False:
			print("Error encountered")
			continue #The continue keyword
		else:
			board = temp_board #update the board if it's not false

		turns = turns + 1 #You can also do turns+=1
runTicTacToe() #calling the function

#testing one two three