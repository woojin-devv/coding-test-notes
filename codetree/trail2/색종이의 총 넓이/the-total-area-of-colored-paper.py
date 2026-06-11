n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100
SIZE = OFFSET * 2

grid = [[0] * SIZE for _ in range(SIZE)]

for x, y in points:
    for row in range(y, y + 8):
        for col in range(x, x + 8):
            grid[row + OFFSET][col + OFFSET] = 1

cnt = 0
for i in range(SIZE):
    for j in range(SIZE):
        if grid[i][j] == 1:
            cnt += 1

print(cnt)