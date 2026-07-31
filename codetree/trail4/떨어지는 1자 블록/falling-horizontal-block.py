n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

answer_grid = [row[:] for row in grid]

# 입력 열 번호를 0-based로 변경
k -= 1

def print_answer(arr):
    for row in arr:
        print(*row)


# 블록이 차지하는 열에서 가장 위쪽에 있는 기존 블록의 행 찾기
top_row = n

for i in range(n):
    for j in range(k, k + m):
        if grid[i][j] == 1:
            top_row = i
            break

    if top_row != n:
        break


# 기존 블록 바로 위에 배치
drop_row = top_row - 1

for j in range(k, k + m):
    answer_grid[drop_row][j] = 1


print_answer(answer_grid)