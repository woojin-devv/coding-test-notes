def solution(my_string):
    answer = ''
    temp = my_string.lower()
    
    arr = list(temp)
    arr.sort()
    
    for el in arr:
        answer += el
            
    return answer