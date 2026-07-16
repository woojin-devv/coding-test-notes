def solution(n):
    NUM = 1_000_000_007
    answer = 0
    dp = [0] * (n+1)
    
    for i in range(1, n+1):
        if i == 1 or i == 2:
            dp[i] = i
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % NUM 
    
    answer = dp[n] % NUM 
    
    return answer

# n = 1 -> 1
# n = 2 -> 2
# n = 3 -> 3
# n = 4 -> 5
# n = 5 -> 