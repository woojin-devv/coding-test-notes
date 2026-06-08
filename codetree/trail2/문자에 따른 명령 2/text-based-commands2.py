dirs = input()

x, y = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

d_i = 0

for d in dirs:
    if d == "L":
        d_i = (d_i - 1) % 4
    elif d == "R":
        d_i = (d_i + 1) % 4
    elif d == "F":
        x += dx[d_i]
        y += dy[d_i]

print(x, y)