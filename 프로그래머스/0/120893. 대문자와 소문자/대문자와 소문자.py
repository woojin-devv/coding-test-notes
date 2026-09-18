def solution(my_string):
    answer = ''
    
    for el in my_string:
        if el.islower():
            answer += el.upper()
        else:
            answer += el.lower()
    return answer