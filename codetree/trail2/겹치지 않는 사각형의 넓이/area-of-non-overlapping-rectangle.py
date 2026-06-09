x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split()) # A
x1[1], y1[1], x2[1], y2[1] = map(int, input().split()) # B
x1[2], y1[2], x2[2], y2[2] = map(int, input().split()) # M

OFFSET = 1000

grid = [[0] * OFFSET * 2 for _ in range(OFFSET * 2)]

def fill_square(x1, x2, y1, y2):
    x1, x2, y1, y2 = map(lambda x: x + OFFSET, (x1, y1, x2, y2))
    for i in range(y1, y2):
        for j in range(x1, x2):
            grid[i][j] = 1

def remove_square(x1, x2, y1, y2):
    x1, x2, y1, y2 = map(lambda x: x + OFFSET, (x1, y1, x2, y2))
    for i in range(y1, y2):
        for j in range(x1, x2):
            if grid[i][j] >= 1:
                grid[i][j] = 0

fill_square(x1[0], y1[0], x2[0], y2[0])
fill_square(x1[1], y1[1], x2[1], y2[1])
remove_square(x1[2], y1[2], x2[2], y2[2])

cnt = 0
for row in grid:
    for el in row:
        if el == 1:
            cnt +=1

print(cnt)