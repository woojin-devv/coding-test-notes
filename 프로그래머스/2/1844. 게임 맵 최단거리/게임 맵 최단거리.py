from collections import deque

# bfs 최단거리 경로 문제
def solution(maps):
    answer = 0
    q = deque()
    
    # 이동 가능 경로 -> 동, 서, 남, 북
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    
    # 방문 초기화 
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    
    # 초기 좌표 q에 append (0, 0)
    q.append([0, 0, 1])
    
    def bfs():
        while q:
            x, y, time = q.popleft()
            
            if x == len(maps) -1  and y == len(maps[0]) -1:
                return time
                
            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy 
                
                # 이동 가능 -> deque에 append, 방문처리
                if (
                    0 <= nx < len(maps)
                    and 0 <= ny < len(maps[0])
                    and not visited[nx][ny] 
                    and maps[nx][ny]
                   ):
                    q.append([nx, ny, time + 1])
                    visited[nx][ny] = True
        return -1
        
    answer = bfs()
    
    return answer