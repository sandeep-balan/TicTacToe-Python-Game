# BOARD
board=['-','-','-',
	   '-','-','-',
	   '-','-','-']

# VARIABLES
player="X"
game_still_going=True

# DISPLAY THE BOARD
def display_board():
	print(board[0],' | ',board[1],' | ',board[2])
	print(board[3],' | ',board[4],' | ',board[5])
	print(board[6],' | ',board[7],' | ',board[8])


# TO GET THE POSITION FROM THE PLAYER
def user_input():
	global player
	print()
	print(player,"'S Turn")
	print()
	position=input("Enter a position from [1-9] : ").strip()

	# CHECK IF POSITION IS IN [1-9]
	while position not in ['1','2','3','4','5','6','7','8','9']:
		position=input("Enter a position from [1-9] : ").strip()

	# CHECK IF POSITION IS OVER WRITE	
	while True:
		if board[int(position)-1]=='-':
			break
		else:
			print("You can't go there !!")
			position=input("Enter a position from [1-9] : ").strip()

	position=int(position)-1

	# INITIALISE THE POSITION ON THE BOARD
	board[position]=player
	print()
	
# TO FLIP THE CURRENT PLAYER
def flip_player():
	global player
	if player=="X":
		player="O"
	elif player=="O":
		player="X"

# CHECK IF PLAYER IS WIN
def is_winner():
	if 	board[0]==board[1]==board[2]==player or\
		board[3]==board[4]==board[5]==player or\
		board[6]==board[7]==board[8]==player or\
		board[0]==board[3]==board[6]==player or\
		board[1]==board[4]==board[7]==player or\
		board[2]==board[5]==board[8]==player or\
		board[0]==board[4]==board[8]==player or\
		board[2]==board[4]==board[6]==player:
			return True
	else:
		return False

# CHECK IF TIE
def is_tie():
	if '-' not in board:
		return True
	else:
		return False

# LET'S PLAY A GAME
def play_game():
	global game_still_going,player
	while game_still_going:
		display_board()
		
		user_input()
		
		if is_winner():
			game_still_going=False
			display_board()
			print()
			print(player," Won.")
		
		elif is_tie():
			game_still_going=False
			display_board()
			print()
			print("Tie")
		
		flip_player()


play_game()