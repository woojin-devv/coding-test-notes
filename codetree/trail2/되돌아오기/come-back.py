N = int(input())
moves = [tuple(input().split()) for _ in range(N)]

# 동, 남, 서, 북
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

mapper = {
    'E': 0,
    'S': 1,
    'W': 2,
    'N': 3
}

x, y = 0, 0
cnt = 0
flag = False

for direction, distance in moves:
    distance = int(distance)

    for _ in range(distance):
        x += dxs[mapper[direction]]
        y += dys[mapper[direction]]
        cnt += 1

        if x == 0 and y == 0:
            flag = True
            break

    if flag:
        break

if flag:
    print(cnt)
else:
    print(-1)