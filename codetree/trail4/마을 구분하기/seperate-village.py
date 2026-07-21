import sys
sys.setrecursionlimit(10 ** 4)

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
answer = []

# 북 -> 북동 -> 동 -> 동남 -> 남 -> 남서 -> 서 -> 북서
# dxs = [-1, -1, 0, 1, 1, 1, 0, -1]
# dys = [0, 1, 1, 1, 0, -1, 0, -1]

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(i, j):
    cnt = 1
    for nx, ny in zip(dxs, dys):
        if in_range(i + nx, j + ny) and not visited[i + nx][j + ny] and grid[i + nx][j + ny]:
            visited[i + nx][j + ny] = True
            cnt += dfs(i + nx, j + ny)
    return cnt 

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j]:
            visited[i][j] = True
            answer.append(dfs(i, j))

# 출력
answer.sort()
print(len(answer))
for el in answer:
    print(el)