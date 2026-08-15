n = int(input())
m = list(map(int, input().split()))

dp = [0] * n

def init():
    for i in range(n):
        dp[i] = 1

init()

for i in range(1, n):
    for j in range(i):
        if m[j] < m[i]:
            dp[i] = max(dp[i], dp[j] + 1)

ans = 0

for i in range(n):
    ans = max(ans, dp[i])

print(ans)