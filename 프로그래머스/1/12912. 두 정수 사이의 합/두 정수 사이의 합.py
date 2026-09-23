def solution(a, b):
    answer = 0
    x = max(a, b)
    y = min(a, b)
    
    for i in range(y, x + 1):
        answer += i
    return answer