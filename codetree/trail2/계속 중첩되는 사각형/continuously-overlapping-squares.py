n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

OFFSET = 101
flag = True

grid = [[0] * OFFSET * 2 for _ in range(OFFSET * 2)]

for x1, y1, x2, y2 in zip(x1, y1, x2, y2):
    x1, y1, x2, y2 = map(lambda x: x + OFFSET, (x1, y1, x2, y2))
    for row in range(y1, y2):
        for col in range(x1, x2):
            if flag:
                grid[row][col] = 'R'
            else:
                grid[row][col] = 'B'
    flag = not flag
cnt = 0
for row in range(len(grid)):
    for col in range(len(grid)):
        if grid[row][col] == 'B':
            cnt += 1

print(cnt)