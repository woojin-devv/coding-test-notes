from itertools import combinations

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = 0 


# 상, 우, 하, 좌
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# 격자 안에 있는지
def in_range(nx, ny):
    return 0 <= nx < n and 0 <= ny < m

for x in range(n):
    for y in range(m):
        neighbors = []
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m:
                neighbors.append(grid[nx][ny])
                
        for a, b in combinations(neighbors, 2):
            answer = max(answer, a + b + grid[x][y])

print(answer)