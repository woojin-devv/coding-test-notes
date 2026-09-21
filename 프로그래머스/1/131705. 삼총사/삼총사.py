def solution(number):
    answer = 0
    visited = [False] * len(number)
    
    def dfs(start, cnt, total):
        nonlocal answer
        
        if cnt == 3:
            if total == 0:
                answer += 1
            return 
        
        for i in range(start, len(number)):
            dfs(i + 1, cnt + 1, total + number[i])
        
    dfs(0, 0, 0)
            
    return answer