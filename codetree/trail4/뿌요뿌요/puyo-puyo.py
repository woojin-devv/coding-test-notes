n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(temp, x, y):
    cnt = 1
    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy

        if(
            in_range(nx, ny) 
            and not visited[nx][ny]
            and temp == grid[nx][ny]
        ):
            visited[nx][ny] = True
            cnt += dfs(temp, nx, ny)

    return cnt
    
answer = []
# 인접할 조건 1. 상하좌우, 2. 인접한 수 = 동일한 수
for i in range(n):
    for j in range(n):
        if not visited[i][j] : 
            visited[i][j] = True
            temp = grid[i][j]
            block = dfs(temp, i, j)

            answer.append(block)
# 출력  (터진 블럭의 수, 최대 블럭의 크기)
max_el = 0
result = 0 
for el in answer:
    if el >= 4:
        result += 1
    max_el = max(max_el, el)

print(f"{result} {max_el}")