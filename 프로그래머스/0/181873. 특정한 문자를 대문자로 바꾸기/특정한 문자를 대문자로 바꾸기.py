def solution(my_string, alp):
    answer = ''
    arr = list(my_string)
    
    for el in arr:
        if el == alp:
            answer += el.upper()
        else:
            answer += el
        
    return answer