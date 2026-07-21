from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
points = [tuple(map(int, input().split())) for _ in range(k)]
visited = [[False] * n for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return(
        in_range(x, y)
        and not visited[x][y]
        and grid[x][y] == 0
    )

def bfs(x, y):
    q = deque([(x, y)])
    visited[x][y] = True
    cnt = 1

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
                cnt += 1
    
    return cnt

cnt = 0 

for x, y in points:
    if not visited[x-1][y-1]:
        cnt += bfs(x-1, y-1)

print(cnt)