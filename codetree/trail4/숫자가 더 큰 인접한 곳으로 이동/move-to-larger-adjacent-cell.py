n, r, c = map(int, input().split())
a = [[0] * (n + 1) for _ in range(n + 1)]
close = False

for i in range(1, n + 1):
    row = list(map(int, input().split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

answer = [a[r][c]]
# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def can_move(nx, ny, center):
    if in_range(nx, ny) and center < a[nx][ny]:
        return True
    return False

def in_range(x, y):
    return 0 <= x <= n and 0 <= y <= n

while True:
    moved = False

    for dx, dy in zip(dxs, dys):
        nx = r + dx
        ny = c + dy
    
        if can_move(nx, ny, a[r][c]):
            answer.append(a[nx][ny])
            r, c = nx, ny
            moved = True
            break
    
    if not moved:
        break

print(*answer)

