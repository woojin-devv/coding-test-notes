n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
answer = -1

def is_positive(r1, c1, r2, c2):
    for i in range(r1, r2 + 1):
        for j in range(c1, c2 + 1):
            if grid[i][j] <= 0:
                return False      
    return True

# 왼쪽 위 좌표 
for r1 in range(n):
    for c1 in range(m):

        # 오른쪽 위 좌표 
        for r2 in range(r1, n):
            for c2 in range(c1, m):
                if is_positive(r1, c1, r2, c2):
                    height = r2 - r1 + 1
                    width = c2 - c1 + 1

                    answer = max(answer, height * width)

print(answer)

