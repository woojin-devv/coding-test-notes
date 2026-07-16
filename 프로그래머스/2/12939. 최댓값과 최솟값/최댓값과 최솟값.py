def solution(s):
    answer = ''
    
    list_a = s.split() 
    list_int = list(map(int, list_a))
    
    min_int = min(list_int)
    max_int = max(list_int)
    
    answer = str(min_int) + ' '+ str(max_int)
    return answer