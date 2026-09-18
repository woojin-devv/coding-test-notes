def solution(sides):
    answer = 0
    # 가장 긴 변 
    long_side = max(sides)
    
    # 남은 변 
    other_sum = sum(sides) - long_side
    
    if long_side < other_sum:
        answer = 1
    else:
        answer = 2
        
    return answer