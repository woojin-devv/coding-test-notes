import sys

sys.setrecursionlimit(10000)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs = [1, 0]
dys = [0, 1]
visited = [[False] * m for _ in range(n)]
x, y = 0, 0

def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

def can_go(x, y):
    if in_range(x, y) and grid[x][y] == 1 and not visited[x][y]:
        return True
    return False

def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if can_go(nx, ny):
            visited[nx][ny] = True
            
            if dfs(nx, ny):
                return 1
    
    return 0


visited[0][0] = True
print(dfs(0, 0))
    
