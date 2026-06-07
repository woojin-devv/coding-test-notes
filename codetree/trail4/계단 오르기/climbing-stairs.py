n = int(input()) # 2 <= N <= 1_000
NUM = 10_007
# n = 2 -> 1
# n = 3 -> 1
# n = 4 -> 1
# n = 5 -> 
# n = 6 -> 

dp = [0] * (n+1)

for i in range(2, n+1):
    if i <= 4:
        dp[i] = 1
    else:
        dp[i] = dp[i-2] + dp[i-3]


print(dp[n] % NUM)