board = [list(map(int, input().split())) for _ in range(19)]
white = 0
black = 0
black_center = (0, 0)
white_center = (0, 0)

def in_range(x, y):
    return 0 <= x < 19 and 0 <= y < 19

def is_vertical_bingo(i, j, color):
    if in_range(i-2, j) and in_range(i+2, j):
        for offset in range(-2, 3):
            x = i + offset
            if board[x][j] == 0 or board[x][j] != color:
                return False
        return True
    return False

def is_horizontal_bingo(i, j, color):
    if in_range(i, j-2) and in_range(i, j+2):
        for offset in range(-2, 3):
            y = j + offset
            if board[i][y] == 0 or board[i][y] != color:
                return False
        return True
    return False

def is_left_diagonal_bingo(i, j, color):
    if in_range(i-2, j-2) and in_range(i+2, j+2):
        for offset in range(-2, 3):
            x, y = i + offset, j + offset
            if board[x][y] == 0 or board[x][y] != color:
                return False
        return True
    return False

def is_right_diagonal_bingo(i, j, color):
    if in_range(i+2, j-2) and in_range(i-2, j+2):
        for offset in range(-2, 3):
            x = i + (offset * (-1))
            y = j + offset 
            if board[x][y] == 0 or board[x][y] != color:
                return False
        return True
    return False

for i in range(19):
    for j in range(19):
        # i, j는 center라고 가정
        if board[i][j] == 1:
            if (is_vertical_bingo(i, j, 1)
                or is_horizontal_bingo(i, j, 1) 
                or is_left_diagonal_bingo(i, j, 1)
                or is_right_diagonal_bingo(i, j, 1)):
                black = 1
                black_center = (i+1, j+1)

        elif board[i][j] == 2:
            if (is_vertical_bingo(i, j, 2)
                or is_horizontal_bingo(i, j, 2) 
                or is_left_diagonal_bingo(i, j, 2)
                or is_right_diagonal_bingo(i, j, 2)):
                white = 1
                white_center = (i+1, j+1)

if (white == 0 and black == 0) or (white == 1 and black == 1):
    print(0)
elif white == 1 and black == 0:
    print(2)
    print(*white_center)
else:
    print(1)
    print(*black_center)

