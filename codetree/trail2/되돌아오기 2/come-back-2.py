commands = input()

# 동남서북
dxs, dys = [1, 0, -1, 0], [0, -1, 0, 1]

# F - 한 칸 이동 
# L - 왼쪽 90도 
# R - 오른쪽 90도

# 처음 위치 
x, y = 0, 0
idx = 3 # 북
cnt = 0
flag = False

for command in commands:
    if command == 'F':
        x, y = x + dxs[idx], y + dys[idx]
    elif command == 'L':
        idx = (idx - 1) % 4
    elif command == 'R':
        idx = (idx + 1) % 4
    cnt += 1

    if x == 0 and y == 0:
        flag = True
        print(cnt)
        break

if not flag:
    print(-1)

