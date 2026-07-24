from collections import deque

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
r, c = map(int, input().split())

r -= 1
c -= 1

# 상, 하, 좌, 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def find_next_position(start_r, start_c):
    current_value = grid[start_r][start_c]

    visited = [[False] * n for _ in range(n)]
    q = deque([(start_r, start_c)])
    visited[start_r][start_c] = True

    candidates = []

    while q:
        x, y = q.popleft()

        for dx, dy in zip(dxs, dys):
            nx = x + dx
            ny = y + dy

            if (
                in_range(nx, ny)
                and not visited[nx][ny]
                and grid[nx][ny] < current_value
            ):
                visited[nx][ny] = True
                q.append((nx, ny))
                candidates.append((grid[nx][ny], nx, ny))

    if not candidates:
        return None

    # 값은 큰 순서, 행과 열은 작은 순서
    candidates.sort(key=lambda position: (-position[0], position[1], position[2]))

    _, next_r, next_c = candidates[0]
    return next_r, next_c


for _ in range(k):
    next_position = find_next_position(r, c)

    if next_position is None:
        break

    r, c = next_position

print(r + 1, c + 1)