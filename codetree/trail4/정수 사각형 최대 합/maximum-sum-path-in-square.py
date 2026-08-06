n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for j in range(n):
    dp[0][j] = dp[0][j-1] + grid[0][j]

for i in range(n):
    dp[i][0] = dp[i-1][0] + grid[i][0]

for i in range(1, n):
    for j in range(1, n):
        dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

if n == 1:
    for row in grid:
        for el in row:
            print(el)
else:
    print(dp[n-1][n-1])