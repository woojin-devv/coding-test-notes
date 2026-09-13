def solution(triangle):
    answer = 0
    # triangle의 높이가 1일 경우 -> triangle[0][0] 반환
    if len(triangle) == 1 :
        answer = triangle[0][0]
    
    else:
        # traingle의 높이가 2일 경우 -> 
        dp = [[0] * (i + 1) for i in range(len(triangle))]
        dp[0][0] = triangle[0][0]

        # dp 초기화 잘 되었는지 확인
        # for row in dp:
        #     print(row)

        # 왼쪽 아래 방향 대각선 dp 채우기
        prev = dp[0][0]
        for i in range(1, len(triangle)):
            dp[i][0] = prev + triangle[i][0]
            prev = dp[i][0] 

        # 오른쪽 아래 방향 대각선 dp 채우기 
        prev = dp[0][0]
        for i in range(1, len(triangle)):
            dp[i][i] = prev + triangle[i][i]
            prev = dp[i][i]
        
        if len(triangle) >= 3:
            # 가운데 구하기 
            for i in range(2, len(triangle)):
                for j in range(1, i):
                    dp[i][j] = max(dp[i-1][j-1] + triangle[i][j], 
                                   dp[i-1][j] + triangle[i][j])
                    
        answer = max(dp[-1])
        
    return answer