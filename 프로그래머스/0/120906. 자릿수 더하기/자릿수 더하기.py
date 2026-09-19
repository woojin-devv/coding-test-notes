def solution(n):
    answer = 0
    arr = list(str(n))
    
    for el in arr:
        answer += int(el)
    return answer