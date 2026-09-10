n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [[False] * n for _ in range(n)]

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

answers = []

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    return (in_range(x, y) 
        and not visited[x][y]
        and grid[x][y] == 1)

def dfs(x, y):
    count = 1 

    for dx, dy in zip(dxs, dys):
        nx = x + dx
        ny = y + dy 

        if can_go(nx, ny):
            visited[nx][ny] = True
            count += dfs(nx, ny)

    return count

for i in range(n):
    for j in range(n):
        if not visited[i][j] and grid[i][j] == 1:
            visited[i][j] = True
            temp = dfs(i, j)
            answers.append(temp)

answers.sort()

print(len(answers))
for answer in answers:
    print(answer)