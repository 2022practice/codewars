def get_board(board):
    board_ = []
    for l in board:
        for item in l:
            if type(item) != str:
                return board
            row = []
            for char in item:
                if char.isdigit():
                    row.append(int(char))
            board_.append(row)
    return board_

def get_row(board, row_num):
    return board[row_num]

def get_col(board,col_num):
    return [ c[col_num] for c in board ]

def get_diag(board,diag_num):
    len_board = len(board)
    if diag_num == 1 :
        return [ board[0][0], board[1][1], board[2][2] ]
    return [ board[2][0], board[1][1], board[0][2] ]

def is_full(board):
    return all( all(r) for r in board) 


def is_solved(board_):
    board = get_board(board_)
    len_board = range(len(board))
    diag_max = 2
    for n in len_board:
        g_r = get_row(board,n)
        g_c = get_col(board,n)
        s_r = list(set(g_r))
        s_c = list(set(g_c))
        if len(s_r) == 1 and s_r[0] != 0:
            return s_r[0]
        if len(s_c) == 1 and s_c[0] != 0:
            return s_c[0]
    for n in range(diag_max):
        g_d = list(set(get_diag(board,n)))
        if len(g_d) == 1 and g_d[0] != 0:
            return g_d[0]
    if is_full(board):
        return 0
    return -1

board = [[0, 0, 1],
         [0, 1, 2],
         [2, 1, 0]] 

assert get_row(board, 0) == [0, 0, 1]
assert get_row(board, 1) == [0, 1, 2]
assert get_row(board, 2) == [2, 1, 0]
assert get_col(board, 0) == [0, 0, 2]
assert get_col(board, 1) == [0, 1, 1]
assert get_col(board, 2) == [1, 2, 0]
assert get_diag(board,1) == [0,1,0]
assert get_diag(board,2) == [2,1,1]
