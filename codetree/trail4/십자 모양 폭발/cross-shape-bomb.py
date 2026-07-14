n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())
r -= 1
c -= 1
offset = grid[r][c] - 1

def in_range(x, y):
    if 0 <= x < n and 0 <= y < n:
        return True
    return False

# 가로 0으로 초기화 
for i in range(c - offset, c + offset + 1):
    if in_range(r, i):
        grid[r][i] = 0

# 세로 0으로 초기화 
for j in range(r - offset, r + offset + 1):
    if in_range(j, c):
        grid[j][c] = 0

# for row in grid:
#     print(row)

# 세로 돌면서 temp랑 swap
for r in range(n):
    temp = []
    for c in range(n-1, -1, -1):
        if grid[c][r] != 0:
            temp.append(grid[c][r])

    zero = n - len(temp)

    for el in range(zero):
        temp.append(0)
    
    # 0으로 초기화
    # c -> 3, 2, 1, 0 
    # temp -> 0, 1

    # c -> 3, 2, 1, 0 
    # n-1 -> 3, 3, 3, 3
    # temp -> 0, 1, 2, 3
    for c in range(n-1, -1, -1):
        grid[c][r] = temp[(n-1)-c]


for row in grid:
    print(*row)