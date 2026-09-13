from collections import deque

def solution(board):
    grid = [ list(el) for el in board]
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    answer = -1
    q = deque()
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    def in_range(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def bfs():

        while q:
            x, y, cnt = q.popleft()
            
            if grid[x][y] == 'G':
                return cnt

            for dx, dy in zip(dxs, dys):

                nx, ny = x, y

                while True: # 장애물 만나기 전까지 계속 직진. 
                    tx = nx + dx
                    ty = ny + dy

                    if not in_range(tx, ty) or grid[tx][ty] == 'D': # 장애물
                        break

                    nx = tx
                    ny = ty

                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny, cnt + 1))
        return -1
                    

    # 시작 지점 찾기 
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'R':
                q.append((i, j, 0))
                answer = bfs()
            
    return answer