n, m = map(int, input().split())
board = [input() for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

#왼쪽
def is_left(i, j):
    if in_range(i, j-2):
        if board[i][j-1] == 'E' and board[i][j-2] == 'E':
            return True
    return False

#오른쪽
def is_right(i, j):
    if in_range(i, j+2):
        if board[i][j+1] == 'E' and board[i][j+2] == 'E':
            return True
    return False

#위
def is_top(i, j):
    if in_range(i-2, j):
        if board[i-1][j] == 'E' and board[i-2][j] == 'E':
            return True
    return False

#아래
def is_bottom(i, j):
    if in_range(i+2, j):
        if board[i+1][j] == 'E' and board[i+2][j] == 'E':
            return True
    return False

#우상향
def is_rt(i, j):
    if in_range(i-2, j+2):
        if board[i-1][j+1] == 'E' and board[i-2][j+2] == 'E':
            return True
    return False

#좌상향
def is_lt(i, j):
    if in_range(i-2, j-2):
        if board[i-1][j-1] == 'E' and board[i-2][j-2] == 'E':
            return True
    return False

#우하향
def is_rb(i, j):
    if in_range(i+2, j+2):
        if board[i+1][j+1] == 'E' and board[i+2][j+2] == 'E':
            return True
    return False

#좌하향
def is_lb(i, j):
    if in_range(i+2, j-2):
        if board[i+1][j-1] == 'E' and board[i+2][j-2] == 'E':
            return True
    return False

# i, j는 L의 위치
cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == "L":
            if is_left(i, j):
                cnt += 1 
            if is_right(i, j):
                cnt += 1
            if is_top(i, j):
                cnt += 1
            if is_bottom(i, j):
                cnt += 1
            if is_rt(i, j):
                cnt += 1
            if is_lt(i, j):
                cnt += 1
            if is_lb(i, j):
                cnt += 1
            if is_rb(i, j):
                cnt += 1

print(cnt)
