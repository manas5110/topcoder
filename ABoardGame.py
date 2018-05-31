def whoWins(finished_board):
	map=[]
	for i in finished_board:
		map.append(list(i))
#	print(map)
#	print("The board looks like below :")
#	print_board(finished_board)
	n=len(finished_board)
	for r in range(0,int(n/2)):
		print("Checking inner square "+str(r+1))
		check_square=[]
		for i in range(int(n/2)-1-r,int(n/2)+1+r):
			for j in range(int(n/2)-1-r,int(n/2)+1+r):
				check_square.append(map[i][j])
		a_count=check_square.count('A')
		b_count=check_square.count('B') 
		if a_count>b_count:
			print('A wins')
			break
		elif b_count>a_count:
			print('B wins')
			break
		else:
			continue
	if a_count==b_count:
		print("It's a draw")


def print_board(in_board):
	print(in_board[0])
	print(in_board[1])
	print(in_board[2])
	print(in_board[3])
	
	
whoWins(['BAAA', 'AAAA','ABBA','AAAA'])