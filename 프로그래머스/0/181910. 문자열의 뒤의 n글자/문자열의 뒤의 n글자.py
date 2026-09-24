def solution(my_string, n):
    answer = ''
    
    start = len(my_string) - n
    answer = my_string[start:]
    
    return answer