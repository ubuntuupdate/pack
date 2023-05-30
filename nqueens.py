n = 4

ld = [0] * 30
rd = [0] * 30
cl = [0] * 30

board = [[0 for i in range(n)] for j in range(n)]

def nqueens(board, col):
    if (col >= n):
        return True
    
    for i in range(n):
        if((ld[i - col + n - 1] != 1 and rd[i + col] != 1) and cl[i] != 1):
            board[i][col] = 1
            ld[i - col + n -1] = rd[i + col] = cl[i] = 1

            if(nqueens(board, col + 1)):
                return True
            
            board[i][col] = 0
            ld[i - col + n -1] = rd[i + col] = cl[i] = 0

    return False

# board = [[0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0],
#          [0,0,0,0]]

# board = [[0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0],
#          [0,0,0,0,0]]

if(nqueens(board, 0) == False):
    print('solution does not exits')
    
for i in range(n):
    for j in range(n):
        print(board[i][j], end=' ')
    print()