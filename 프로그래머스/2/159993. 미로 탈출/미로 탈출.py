from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])

    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]

    def in_range(x, y):
        return 0 <= x < n and 0 <= y < m

    # 시작점, 출구, 레버 위치 찾기
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)
            elif maps[i][j] == 'L':
                lev = (i, j)

    def bfs(start, target):
        # 호출할 때마다 큐와 방문 기록을 새로 생성
        q = deque()
        visited = [[False] * m for _ in range(n)]

        sx, sy = start
        q.append((sx, sy, 0))  # 행, 열, 이동 시간
        visited[sx][sy] = True

        while q:
            x, y, time = q.popleft()

            # 목적지에 도착했다면 최단 시간 반환
            if (x, y) == target:
                return time

            for dx, dy in zip(dxs, dys):
                nx = x + dx
                ny = y + dy

                if (
                    in_range(nx, ny)
                    and not visited[nx][ny]
                    and maps[nx][ny] != 'X'
                ):
                    visited[nx][ny] = True
                    q.append((nx, ny, time + 1))

        # 목적지에 도착하지 못한 채 탐색 종료
        return -1

    start_to_lev = bfs(start, lev)
    if start_to_lev == -1:
        return -1

    lev_to_end = bfs(lev, end)
    if lev_to_end == -1:
        return -1

    return start_to_lev + lev_to_end