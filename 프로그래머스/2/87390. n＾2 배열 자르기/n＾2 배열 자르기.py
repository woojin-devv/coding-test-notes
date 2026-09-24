def solution(n, left, right):
    answer = []

    for idx in range(left, right+1):
        j = idx % n 
        i = idx // n
            
        element = 0
        
        if i - j < 0:
            temp = 0
        else:
            temp = i - j
            
        element += temp + (j + 1)
        answer.append(element)
        
    return answer