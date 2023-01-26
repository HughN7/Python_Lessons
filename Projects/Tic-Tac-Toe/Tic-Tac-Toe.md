# Creating Tic-Tac-Toe

## 1. Creating the board
The rules of the game are simple: Align three in a row/column/diagonal in order to win

```
   |   |   
-----------
   |   |   
-----------
   |   |
```
We can represent each tile on the board by numbers, for the sake of simplicity, we'll start everything at 0

```
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
```

Because of this, **we can represent our board as a list**:
```python
board = [0,1,2,3,4,5,6,7,8]
```
And if we use ```f strings``` we can print out the board

```python
print(f" {board[0]} | {board[1]} | {board[2]}")
print("-----------")
print(f" {board[3]} | {board[4]} | {board[5]}")
print("-----------")
print(f" {board[6]} | {board[7]} | {board[8]}")

'''
This will print out:
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
'''
```

But because we want to print this multiple times, **we need to re-use our code**. We can do this by making it a function

```python
def printBoard(board): #We are passing the board into this function. If we didn't do this, it will give us an error
	print(f" {board[0]} | {board[1]} | {board[2]}")
	print("-----------")
	print(f" {board[3]} | {board[4]} | {board[5]}")
	print("-----------")
	print(f" {board[6]} | {board[7]} | {board[8]}")

```

## 2. Checking who wins or not
There are 8 ways to win in tic-tac-toe. 
- 3 possible lined up rows
- 3 possible lined up columns
- 2 possible lined up diagonals

We need to program all winning solutions. We'll also need to check this again and again as the game continues. 

To do this, we'll create another function

```python
def findWinner(board):
	#Rows
	#Columns
	#Diagnoals
	#If there isn't a winner yet
```

we'll also need to pass in the board to check the x and o's in the board

```python
def findWinner(board)
	#Rows
 	#Columns
	#Diagnoals
 	#If there isn't a winner yet
```

Now let's start checking the winners for the rows. **Remember that we're representing each tile as a number in the list:**

```
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
```
Therefore to check the first row:
```python
def findWinner(board)
	#Rows
	if board[0] == board[1] == board[2]:
		#Return x or o (The winner)
 	#Columns
	#Diagnoals
 	#If there isn't a winner yet
```
- If tile 0, 1 and 2 are the same then that means that we have a winner right? It's either x or o
- This means that if we want to return the winner (either x or o) **We need to return the value that's stored inside of the row**

Further explanation:
- This is our board:
```
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
```
- If the first row (tiles 0, 1 and 2) we check that there's a winner
```
 x | x | x 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8

or

 o | o | o 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
```

Then we return the winner (x or o), by getting the value (x or o) that's stored in the tiles of the winning row (tiles 0, 1 or 2)
```python
def findWinner(board)
	#Rows
  if board[0] == board[1] == board[2]:
		#Return x or o (The winner)
		return board[0]
		#You can also do:
		#return board[1] or #return board[2]
		#It doesn't matter as long as you return
		#one of the tiles that are part of the winning row
 	#Columns
	#Diagnoals
 	#If there isn't a winner yet
```

**Now that we've checked the first row, we need to check the other rows, the colums and the diagonals**
```python
def findWinner(board):
	#Rows
	if board[0] == board[1] == board[2]:
		return board[0]
	elif board[3] == board[4] == board[5]:
		return board[3]
	elif board[6] == board[7] == board[8]:
		return board[6]
	#Columns
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
```
**But we're not done yet**. What if there isn't a winner yet (What if we only placed two tiles down)? Then we return a value that is not x or o. We'll use the boolean value `False` in this case. 

```python
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
```

## 3. Function to Place X and O onto the board
Similar to checking for who's the winner, we need a function to place X and O onto the board. We'll pass board here as well to modify it

When we're placing X or O onto the board, we have to ask a few questions.
1. Which player's turn is it? X or O?
2. Which tile are they choosing?
	1. Remember, we're representing each tile by its number

We can use inputs for these
```python
'''
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
'''

def placeXO(board):
	
	print("Who's turn is it? X or O?")
	player = input() #Enter X or O

	print("Which tile do you want to choose?")
	tile_number = int(input()) #0-8
```

To place X or O onto the board, all we have to do is use the two variables `player` and `tile_number` in order to access the list (the board) and assign it. 
- Remember, the board is a list. We access and modify the list by accessing the index inside of square brackets. Treat `list[index]` like it's a variable
```python
'''
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
'''

def placeXO(board):
	
	print("Who's turn is it? X or O?")
	player = input() #Enter X or O

	print("Which tile do you want to choose?")
	tile_number = int(input()) #0-8

	print("Placing", player, "on tile number", tile_number)
	board[tile_number] = player
```

Once we're done modifying the board, we have to return the updated board

```python
'''
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
'''

def placeXO(board):
	
	print("Who's turn is it? X or O?")
	player = input() #Enter X or O

	print("Which tile do you want to choose?")
	tile_number = int(input()) #0-8

	print("Placing", player, "on tile number", tile_number)
	board[tile_number] = player

	return board
```


**But, we're not done**

## 4. We still gotta check for ties and errors
- What if there is a tie?
- What if the player didn't enter x or o?
- What if the player entered a tile number that's not from 0 to 9?
- What if the player chooses a tile that already has x and o in it?

We still have to make our game check all these conditions

### 4.1. Let's check if the player accidentally entered something that's not X or O
This is pretty simple, all we need is an if statement after we ask the player to enter x or o. 
- If they didn't enter X or O, we make the function return `False` instead of the board

```python
'''
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
'''

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

	print("Placing", player, "on tile number", tile_number)
	board[tile_number] = player

	return board
```


### 4.3. Check if the player accidentally entered a tile number that's not 0-8:
All we need here is an `if` statement that checks the value inputted. It's very similar to the previous error check we made.

```python
'''
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
'''

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

	print("Placing", player, "on tile number", tile_number)
	board[tile_number] = player

	return board
```

### 4.4. Check if the player chose a tile that already has x or o in it:
We first need to access the value that's stored inside of the tile. If the value stored in it is either `x` or `o` then that means that someone has already taken it and it's invalid. If it's invalid then we just tell again return `False`

```python
'''
 0 | 1 | 2 
-----------
 3 | 4 | 5 
-----------
 6 | 7 | 8
'''

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
```

## 5. Bringing everything together in the main game

Now let's make a single function that runs the entire game. And if we want to run the game we need to call it
```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")

runTicTacToe() #calling the function
```

We're going to be using all the functions that we've created so far `PrintBoard()`, `FindWinner()`, `PlaceXO()`. 
- Remember that we mentioned way earlier that we're also representing the board as a list

```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

runTicTacToe() #calling the function
```

Now, **Every single game in existence**, be it Minecraft, Roblox, Elden Ring, etc. Is just a single giant loop that runs forever unless there's a condition that stops the loop. So we're also going to make a game loop here. 

```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

	while True: #The game loop
		...

runTicTacToe() #calling the function
```

The first thing we want to do is to print the board so that the players can see what's going on right? Therefore we need to call the `printBoard()` function we made and pass `board` into it

```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

	while True: #The game loop
		printBoard(board)

runTicTacToe() #calling the function
```

Every single time the game runs, we also need to check if there's a winner or not right? So we'll do that as well by calling the `findWinner()` function 
- Remember that `findWinner()` **returns** either a winner (X or O) or `False` if there's no winner
- When we return stuff we can assign the thing that's returned into a variable. Let's also create a variable then called `winner`

```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

	while True: #The game loop
		printBoard(board)
		winner = findWinner(board)

runTicTacToe() #calling the function
```

At this point if there is a winner, the variable `winner` will contain X or O. 
- Therefore we'll need to stop the game

But if there's no winner (`winner` doesn't contain X or O. Then we'll just continue the game)
- We can make this easier for ourselves by checking if `winner` contains `False` or not since `findWinner()` can return False

```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

	while True: #The game loop
		printBoard(board)
		winner = findWinner(board)
		if winner != False:
			print("The winner is: ", winner)
			return

runTicTacToe() #calling the function
```

Again, at this point, **If there's no winner the game continues**
- If the game continues, we gotta place X or O onto the board right?
- This is why we created to `placeXO()` function. 
- Similar to what we did to `findWinner()`, we'll call `placeXO()`

Remember that `placeXO()`
- Returns an updated board
- **OR** returns `False` if there's an error
	- This means that it might might not immediately give us an updated board.
	- So **let's create a temporary variable to check if `placeXO()` returns `False` or returns an updated board first**
	- If `placeXO()` returns `False`, **we'll use the `continue` keyword to skip to the next loop**
- If it's not `False`, we'll update the board

```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

	while True: #The game loop
		printBoard(board)
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

runTicTacToe() #calling the function
```


**We're almost finished**. We're missing one last thing
- What if the game ends with a Tie? We were suppose to do this earlier in `placeXO()` but it's easier if we check if the game ties or not in `runTicTacToe()`

Remember that there are 9 tiles in Tic-Tac-Toe. Which means that in total, you can only place something on the board 9 times. 
- Ergo: There are only 9 turns possible in Tic-Tac-Toe. 
- When we placed `findWinner()` inside of the game loop, we're only checking if there's a winner or not. 
- **Tic-Tac-Toe ties only if by the end of the 9 turns, there is no winner**
- So we need a way to track how many turns have been played so far. 
	- We can do this by created a variable, let's call it `turns`. 
	- We'll set this to 1 at first for "turn 1"
	- By the end of the game loop, if the game is still on-going we'll increase the value of `turns` by 1

```python
def runTicTacToe():
	print("Welcome to Tic-Tac-Toe")
	board = [0,1,2,3,4,5,6,7,8]

	turns = 1
	while True: #The game loop
		printBoard(board)
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
```


At this point, all we have to do is check if turns is greater than 9.
- Again the **total possible turns** is 9. 
- If the variable `turns` becomes say 10, that means the game has tied right? Since it isn't possible to have 10 turns
- We can do this by having an if statement at the beginning of the loop

```python
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
```


## 6. So you've made Tic-Tac-Toe
```python
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
```

## Now... How do you program the AI? ;)
