def solution(s):
    answer = True
    
    if len(s) == 4 or len(s) == 6:
        arr = list(s)
        
        for el in arr:
            if not el.isdigit():
                answer = False
                break
    else:
        answer = False
    return answer