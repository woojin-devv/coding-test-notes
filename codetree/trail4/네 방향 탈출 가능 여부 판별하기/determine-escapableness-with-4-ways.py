from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y):
    return (
        in_range(x, y)
        and not visited[x][y]
        and a[x][y]
        )

def bfs(start_x, start_y):
    q = deque([(start_x, start_y)])

    while q:
        x, y = q.popleft()

        if x == n - 1 and y == m - 1:
            return 1

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
    return 0

print(bfs(0, 0))