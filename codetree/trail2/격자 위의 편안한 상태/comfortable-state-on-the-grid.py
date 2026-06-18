n, m = map(int, input().split())
points = [tuple(map(int, input().split())) for _ in range(m)]

grid = [[0] * (n+1) for _ in range(n+1)]

#상, 하, 좌, 우
dxs, dys = [0, 0, -1, 1], [-1, 1, 0, 0]

def in_range(x, y, n):
    if 1 <= x and x < n + 1 and 1 <= y and y < n+1:
        return True
    return False

# grid에 색칠
for i in range(m):
    r, c = points[i]
    grid[r][c] = 1
    cnt = 0
    for m_x, m_y in zip(dxs, dys):
        if in_range(r + m_y, c + m_x, n) and grid[r+m_y][c+m_x] == 1:
            cnt +=1
    if cnt == 3:
        print(1)
    else:
        print(0)


    