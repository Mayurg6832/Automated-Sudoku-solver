board=[
	[1,0,0,0,0,0,4,0,0],
	[0,6,7,0,0,2,0,0,0],
	[0,0,0,0,0,0,6,0,3],
	[0,0,0,0,3,4,0,9,8],
	[0,0,0,6,8,0,0,0,0],
	[0,5,0,0,1,0,0,0,0],
	[4,0,5,0,0,0,0,7,0],
	[0,7,6,0,0,0,0,0,0],
	[0,0,0,0,0,3,0,5,0]
]

def fill(board):
	box=find_empty(board)
	if not box:
		return True
	else:
		r,c=box
	
	for i in range(1,10):
		if is_valid(board,i,(r,c)):
			board[r][c]=i

			if fill(board):
				return True
			board[r][c]=0
	return False

def is_valid(board,num,pos):
	
	for i in range(9):
		if board[pos[0]][i]==num and pos[1]!=i:
			return False

	for i in range(9):
		if board[i][pos[1]]==num and pos[0]!=i:
			return False
	
	board_x=pos[1]//3
	board_y=pos[0]//3
	for i in range(board_y*3,board_y*3+3):
		for j in range(board_x*3,board_x*3+3):
			if board[i][j]==num and (i,j)!=pos:
				return False
	return True


	

def find_empty(board):
	for i in range(9):
		for j in range(9):
			if board[i][j]==0:
				return (i,j)

def board_print(board):
	for i in range(9):
		if i%3==0 and i!=0:
			print('-----------------------')
		
		for j in range(9):
			if j%3==0 and j!=0:
				print(' | ',end="")
			
			if j==8:
				print(board[i][j])
			else:
				print(str(board[i][j])+" ",end="")
		

board_print(board)
fill(board)
print('===================')
board_print(board)
