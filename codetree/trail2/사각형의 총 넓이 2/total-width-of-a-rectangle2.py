n = int(input())
OFFSET = 100

grid = [[0] * OFFSET * 2 for _ in range(OFFSET * 2)]

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    x1, y1, x2, y2 = map(lambda x: x + OFFSET, (x1, y1, x2, y2))

    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

cnt = 0
for row in grid:
    for el in row:
        if el == 1:
            cnt += 1

print(cnt)