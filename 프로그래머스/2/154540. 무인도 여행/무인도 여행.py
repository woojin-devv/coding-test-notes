from collections import deque
def solution(maps):
    answer = []
    q = deque()
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    grid = [list(el) for el in maps]
    visited = [[False] * len(grid[0]) for _ in range(len(grid))]
    
    def bfs(curr):
        
        while q:
            x, y= q.popleft()
            
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy 
                
                if (0 <= nx < len(grid)
                    and 0 <= ny < len(grid[0])
                    and not visited[nx][ny]
                    and grid[nx][ny] != 'X'):
                    
                    visited[nx][ny] = True
                    q.append((nx, ny))
                    curr += int(grid[nx][ny])
        return curr
                    
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (
            not visited[i][j] 
            and grid[i][j] != 'X'
            ):
                visited[i][j] = True
                q.append((i, j))
                curr = int(grid[i][j])
                
                temp = bfs(curr)
                
                answer.append(temp)
                
    if len(answer) == 0:
        answer.append(-1)
    answer.sort()

    return answer