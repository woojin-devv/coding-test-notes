n, m = map(int, input().split())
alphabet = ['A', 'B', 'C', 'D', 'E', 
            'F', 'G', 'H', 'I', 'J', 
            'K', 'L', 'M', 'N', 'O', 
            'P', 'Q', 'R', 'S', 'T', 
            'U', 'V', 'W', 'X', 'Y', 'Z']

# alphabet의 length = 26
# 오른, 아래, 왼, 위
dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]

# 기본 초기화
grid = [[0] * m for _ in range(n)]
x, y = 0, 0
curr_dir = 0

def in_range(x, y, n, m):
    if 0 <= x and x < m and 0 <= y and y < n:
        return True
    return False

# grid의 cell의 개수 만큼. 
for cnt in range(n * m):
    i = cnt % 26
    grid[y][x] = alphabet[i]

    if not in_range(x + dxs[curr_dir], y + dys[curr_dir], n, m) or (grid[y + dys[curr_dir]][x + dxs[curr_dir]]) != 0 :
        curr_dir = (curr_dir + 1) % 4

    x, y = x + dxs[curr_dir], y + dys[curr_dir]

for row in grid:
    print(*row)