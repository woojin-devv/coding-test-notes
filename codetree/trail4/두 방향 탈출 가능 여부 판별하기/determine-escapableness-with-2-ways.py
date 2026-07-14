n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

# 동 남 
dxs = [0, 1]
dys = [1, 0]

# 조건 (순서)
    # 1. 오른쪽 진입 
    # 2. 아래 진입 

# 범위 안에 있는지 체크하는 함수 
def in_range(x, y):
    if 0 <= x < n and 0 <= y < m:
        return True
    return False

# can_go 함수
    # 1. 격자 안에 있는 경우 
    # 2. 진입하려고 하는 방향에 뱀이 존재하지 않을 경우 
    # 3. 방문하지 않은 경우
def can_go(nx, ny):
    if not in_range(nx, ny):
        return False
    if grid[nx][ny] == 0:
        return False
    if visited[nx][ny]:
        return False
    return True

# dfs 
def dfs(x, y):
    if x == n - 1 and y == m - 1:
        return 1

    for off_x, off_y in zip(dxs, dys):
        nx = x + off_x
        ny = y + off_y

        if can_go(nx, ny):
            visited[nx][ny] = True
            
            if dfs(nx, ny):
                return True
    return False
    
visited[0][0] = True

if dfs(0, 0):
    print(1)
else:
    print(0)