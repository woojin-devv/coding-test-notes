from collections import deque

def solution(n, wires):
    answer = float('inf')
    grid = [[0] * (n+1) for _ in range(n+1)]
    q = deque()
    
    # 인접행렬로 변환 
    for el in wires:
        a, b = el
        grid[a][b] = 1
        grid[b][a] = 1

    def bfs(start):
        visited = [False] * (n + 1)
        q.append(start)
        visited[start] = True
        cnt = 1  # 시작 송전탑

        while q:
            node = q.popleft()

            # 현재 송전탑과 연결된 송전탑 찾기
            for nxt in range(1, n + 1):
                if (grid[node][nxt] == 1 and not visited[nxt]):
                    visited[nxt] = True
                    q.append(nxt)
                    cnt += 1

        return cnt
        
    for i in range(len(wires)):
        # i는 끊을 전선
        a, b = wires[i]
        grid[a][b] = 0 
        grid[b][a] = 0
        
        # i 스킵 -> n - v1 = v2 -> 구) v2 - v1의 최소 
        v1 = bfs(a)
        
        # 전선 복구
        grid[a][b] = 1 
        grid[b][a] = 1
        
        v2 = n - v1
        answer = min(abs(v2-v1), answer)
        
    return answer