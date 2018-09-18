# ## Board Create ## 
def display_board(board):
    print(board[7]+'|'+board[8]+'|'+board[9])
    print(board[4]+'|'+board[5]+'|'+board[6])
    print(board[1]+'|'+board[2]+'|'+board[3])

# ## Board Test ##
test_board = ['#','X','O','X','O','X','O','X','O','X']
# display_board(test_board)


## Place Marker ##

def place_marker(board, marker, position):
	board[position] = marker
	
# ## Place Marker Test ##
# place_marker(test_board, '$', 8)
# display_board(test_board)

## Win Check ##

def win_check(board, mark): 
	
	return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
	(board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
	(board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
	(board[7] == mark and board[4] == mark and board[1] == mark) or # down the left
	(board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
	(board[9] == mark and board[6] == mark and board[3] == mark) or # down the right
	(board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
	(board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

## Win Check Test ## 
win_check(test_board, 'X')