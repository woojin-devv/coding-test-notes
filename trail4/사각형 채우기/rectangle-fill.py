n = int(input())
NUM = 10_007

# n = 1, 1
# n = 2, 2
# n = 3, 3
# n = 4, 5
# n = 5, 1 + 4 + 3 = 8 
# n = 6, 

dp = [0] * (n+1)


for i in range(1, n+1):
    if i <= 3:
        dp[i] = i
    else:
        dp[i] = dp[i-1] + dp[i-2]

print(dp[n] % NUM)