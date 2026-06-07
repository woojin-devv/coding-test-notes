n = int(input())

# Please write your code here.
board = [[0]*n for _ in range(n)]

current = 1

for i in range(n):
    for j in range(n):
        if current > 9:
            current = 1
        board[i][j] = current
        current += 1

for row in board:
    print(*row)