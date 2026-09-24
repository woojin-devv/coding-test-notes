def solution(sizes):
    answer = 0
    max_max = max(max(row) for row in sizes)
    min_max = max(min(row) for row in sizes)
    
    answer = max_max * min_max
    
    return answer