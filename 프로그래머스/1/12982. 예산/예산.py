def solution(d, budget):
    answer = 0
    
    d.sort()
    
    for cost in d:
        if cost > budget:
            break
        
        budget -= cost
        answer += 1
    return answer