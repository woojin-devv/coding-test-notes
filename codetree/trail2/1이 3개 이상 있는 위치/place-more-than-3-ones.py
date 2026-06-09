n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x, y, n):
    return 0 <= x and x < n and 0 <= y and y < n

cnt = 0
for i in range(n):
    for j in range(n):
        temp = 0
        for dx, dy in zip(dxs, dys):
            nx, ny = i + dx, j + dy
            if in_range(nx, ny, n) and grid[nx][ny] == 1:
                temp +=1
                if temp >= 3:
                    temp = 0
                    cnt += 1

print(cnt) 