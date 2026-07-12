n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

visited = [False] * n
answer = float('-inf')


def backtracking(row, total):
    global answer

    # 0행부터 n-1행까지 모두 선택한 경우
    if row == n:
        answer = max(answer, total)
        return

    # 현재 행에서 선택할 열 결정
    for col in range(n):
        if not visited[col]:
            visited[col] = True

            backtracking(
                row + 1,
                total + grid[row][col]
            )

            # 선택 복구
            visited[col] = False


backtracking(0, 0)

print(answer)