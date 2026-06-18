n, m = map(int, input().split())
grid = [[0] * m for _ in range(n)]

# 아래, 오른쪽, 위쪽, 왼쪽
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 초기 direction 
d_i = 0
x, y = 0, 0

def in_range(x, y, n, m):
    if 0 <= x and x < m and 0 <= y and y < n:
        return True
    return False

for i in range(1, n * m + 1):
    # i번째에 채워질 칸
    grid[y][x] = i
    # x, y 의 값 업데이트 
    if not in_range(x + dxs[d_i], y + dys[d_i], n, m) or grid[y + dys[d_i]][x+dxs[d_i]] != 0 :
        d_i = (d_i + 1) % 4
    x, y = x + dxs[d_i], y + dys[d_i]

for row in grid:
    print(*row)
