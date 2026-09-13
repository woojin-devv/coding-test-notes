from collections import deque

def solution(n, vertex):
    graph = [[] for _ in range(n + 1)]

    for a, b in vertex:
        graph[a].append(b)
        graph[b].append(a)

    def bfs(start):
        visited = [False] * (n + 1)
        distance = [0] * (n + 1)

        q = deque([start])
        visited[start] = True

        while q:
            curr = q.popleft()

            for next_node in graph[curr]:
                if not visited[next_node]:
                    visited[next_node] = True
                    distance[next_node] = distance[curr] + 1
                    q.append(next_node)

        return distance

    distance = bfs(1)
    
    # print(distance)

    max_distance = max(distance)

    return distance.count(max_distance)