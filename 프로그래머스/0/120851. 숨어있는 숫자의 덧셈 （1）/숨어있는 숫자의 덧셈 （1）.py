def solution(my_string):
    answer = 0
    arr = list(my_string)
    
    for el in arr:
        if el.isdigit():
            answer += int(el)
    return answer