def solution(n):
    NUM = 1234567
    dp = [0] * (n+1)
    answer = 0
    
    for i in range(n+1):
        if i == 0 or i == 1:
            dp[i] = i
        else:
            dp[i] = (dp[i-1] + dp[i-2]) % NUM
        
    answer = dp[n] % NUM
    return answer