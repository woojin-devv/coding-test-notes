n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
curr_dir = 0


# grid[y][x]
# (x, y)
# (0, 0), (0, 1), (0, 2), (0, 3)
# (1, 0), (1, 1), (1, 2), (1, 3)
# (2, 0), (2, 1), (2, 2), (2, 3)
# 초기 x, y 값
x, y = 0, 0 

def in_range(x, y, n):
    if 0 <= x and x < m and 0 <= y and y < n:
        return True
    return False

for i in range(n*m):
    if grid[y][x] == 0:
        grid[y][x] = i+1
    if not in_range(x + dxs[curr_dir], y + dys[curr_dir], n) or (grid[y + dys[curr_dir]][x + dxs[curr_dir]] != 0):
        curr_dir = (curr_dir + 1) % 4
    x, y = x + dxs[curr_dir], y + dys[curr_dir]
    

for row in grid:
    print(*row)
