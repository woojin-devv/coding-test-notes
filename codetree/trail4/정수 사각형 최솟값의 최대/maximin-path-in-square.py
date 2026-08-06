n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

# 시작점
dp[0][0] = grid[0][0]

# 첫 번째 행: 왼쪽에서만 올 수 있음
for j in range(1, n):
    dp[0][j] = min(dp[0][j - 1], grid[0][j])

# 첫 번째 열: 위쪽에서만 올 수 있음
for i in range(1, n):
    dp[i][0] = min(dp[i - 1][0], grid[i][0])

# 나머지 칸
for i in range(1, n):
    for j in range(1, n):
        from_top = min(dp[i - 1][j], grid[i][j])
        from_left = min(dp[i][j - 1], grid[i][j])

        dp[i][j] = max(from_top, from_left)

print(dp[n - 1][n - 1])