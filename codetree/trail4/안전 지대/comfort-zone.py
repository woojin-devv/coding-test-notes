import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
max_k = 0

#max_k 초기화
for i in range(n):
    for j in range(m):
       max_k = max(max_k, grid[i][j]) 

# 출력 배열 > 튜플 (k, 안전영역 수 )
answer = []

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs(k, x, y):
    cnt = 1

    for nx, ny in zip(dxs, dys):

        # 조건 
        if in_range(x + nx, y + ny) and not visited[x + nx][y + ny] and grid[x + nx][y + ny] > k:
            visited[x + nx][y + ny] = True
            dfs(k, x + nx, y + ny)

# k 이하일 때, 안전지대
for k in range(1, max_k+1):
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and grid[x][y] > k:
                visited[x][y] = True
                cnt += 1
                dfs(k, x, y)
    answer.append((k, cnt))

# 출력 1
# k(안전영역 최대인 K), 안전 영역 수 
answer.sort(key=lambda x: x[1], reverse=True)

a, b = answer[0]
print(a, b)