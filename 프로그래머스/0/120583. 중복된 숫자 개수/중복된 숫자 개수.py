def solution(array, n):
    answer = 0
    
    for el in array:
        if el == n:
            answer += 1
    return answer