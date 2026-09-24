def solution(num_str):
    answer = 0
    
    for el in num_str:
        answer += int(el)
    return answer