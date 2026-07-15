n, t = map(int, input().split())
str = input()
grid = [list(map(int, input().split())) for _ in range(n)]

# 상 우 하 좌 
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]
idx = 0

center = n // 2
x, y = center, center

# 초기 sum -> 중심점 위치의 값으로 초기화 
answer = grid[x][y]
''' can_go 함수
 1. 가려고 하는 grid[nx][ny]가 범위 내에 존재해야 함
'''
def can_go(x, y):
    return 0 <= x < n and 0 <= y < n

def is_change_direction(c):
    if c == 'R' or c == 'L':   
        return True
    else:
        return False

def set_idx(c):
    global idx

    if c == 'R':
        idx = (idx + 1) % 4
    elif c == 'L':
        idx = (idx - 1) % 4

for i in range(t):
    if is_change_direction(str[i]):
        set_idx(str[i])

    if not is_change_direction(str[i]) and can_go(x + dxs[idx], y + dys[idx]):
        x, y = x + dxs[idx], y + dys[idx]
        answer += grid[x][y]
    else: continue

print(answer)