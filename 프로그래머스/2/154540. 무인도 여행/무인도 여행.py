from collections import deque

def solution(maps):
    grid = []
    
    for i in range(len(maps)):
        grid.append(list(maps[i]))
    
    answers = []
    q = deque()
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    def in_range(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0])
    
    def bfs(start):
        temp = start
        
        while q:
            x, y = q.popleft()
            
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy 
                
                if (
                in_range(nx, ny)
                and not visited[nx][ny]
                and grid[nx][ny] != 'X'
                ):
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    
                    temp += int(grid[nx][ny])
        return temp
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if not visited[i][j] and grid[i][j] != 'X':
    
                visited[i][j] = True
                q.append((i, j))
                start = int(grid[i][j])
                answer = bfs(start)
                
                if answer != 0:
                    answers.append(answer)
    
    answers.sort()
    
    if len(answers) == 0:
        answers.append(-1)
                
    return answers