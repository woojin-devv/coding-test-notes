def solution(numbers, target):
    answer = 0
    
    def dfs(idx, curr):
        nonlocal answer
        
        if idx == len(numbers):
            if curr == target:
                answer += 1
            return 
        
        dfs(idx + 1, curr + numbers[idx])
        dfs(idx + 1, curr - numbers[idx])
        
    dfs(0, 0)
    return answer