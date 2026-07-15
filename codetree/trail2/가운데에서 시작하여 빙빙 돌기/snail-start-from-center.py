n = int(input())
grid = [[0] * n for _ in range(n)]

# n은 항상 홀수 
# 중심점 좌표 구하기 
x, y = n // 2, n // 2

# 회전 순서 : 우, 상, 좌, 하 
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]
idx = 0
cells = n * n 

# grid 중심점 값 초기화 
grid[x][y] = 1
curr = 1
# stride는 방향 전환 하기 전 반복되는 보폭
# 이동 -> 방향전환 -> 이동 -> 방향전환 -> 이동 -> 이동 -> 방향전환 -> 이동 -> 이동 ->
def can_go(x, y):
    return 0 <= x < n and 0 <= y < n

for stride in range(1, n+1):
    # stride => 1, 2, 3, 4
    for _ in range(2):
        for _ in range(stride):
            if curr >= cells:
                break
            # 이동 
            if can_go(x + dxs[idx], y + dys[idx]):
                x, y = x + dxs[idx], y + dys[idx]
                curr += 1
                grid[x][y] = curr
        # 방향전환 
        idx = (idx + 1) % 4

for row in grid:
    print(*row)
            


        
