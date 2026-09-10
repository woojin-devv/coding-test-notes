from collections import deque

n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
# q 초기화 
q = deque()

# 인접 행렬 크기 초기화 
vertexs = [[0] * n for i in range(n)]

# 노드 방문한 구간 초기화 
visited = [False] * n

answer = 0

# edges -> vertex에 대한 인접행렬로 치환 
for a, b in edges:
    a -= 1
    b -= 1

    vertexs[a][b] = 1
    vertexs[b][a] = 1

def bfs(start):
    global answer
    q.append(start)
    visited[start] = True

    while q:
        node = q.popleft()

        for i in range(len(vertexs)):
            if not visited[i] and vertexs[i][node] == 1:
                visited[i] = True
                q.append(i)
                answer += 1
    
bfs(0)

print(answer)