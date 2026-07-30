n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
dys = [-1, 0, 1, 1, 1, 0, -1, -1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def gold_mining(x, y, k):
    gold = 0

    # 중심에서 상하좌우로 k만큼 떨어진 범위 확인
    for i in range(x - k, x + k + 1):
        for j in range(y - k, y + k + 1):

            # 격자 안이고, 다이아몬드 범위 내부인 경우
            if (
                in_range(i, j)
                and abs(x - i) + abs(y - j) <= k
                and grid[i][j] == 1
            ):
                gold += 1

    if pow(k, 2) + pow(k + 1, 2) <= m * gold:
        return gold
    else:
        return 0

    idx = 1
    gold = 0

    for dx, dy in zip(dxs, dys):
        if idx % 2 != 0:
            for i in range(k-1):
                nx = x + dx
                ny = y + dx

                if in_range(nx, ny) and grid[nx][ny] == 1:
                    gold += 1
        else:
            for i in range(k):            
                nx = x + dx
                ny = y + dy 

                if in_range(nx, ny) and grid[nx][ny] == 1:
                    gold += 1
        idx += 1

    if pow(k, 2) + pow(k+1, 2) <= m * gold :
        return gold 
    else:
        return 0

answer = float('-inf')

for k in range(n + 1):
    for i in range(n):
        for j in range(n):
            gold = gold_mining(i, j, k)
            answer = max(answer, gold)

print(answer)