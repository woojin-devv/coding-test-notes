n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]
visited = [False] * (n + 1)
# n = 정점, m = 간선
# 인접 행렬 초기화 
cost = [[0] * (n+1) for _ in range(n+1)]
vc = 0
# 인접 행렬에 간선 연결 
for i, j in edges:
    cost[i][j] = 1
    cost[j][i] = 1

visited[1] = True

def dfs(v):
    global vc

    for curr_v in range(1, n+1):
        if cost[v][curr_v] and not visited[curr_v]:
            visited[curr_v] = True
            dfs(curr_v)
            vc += 1

dfs(1)
print(vc)