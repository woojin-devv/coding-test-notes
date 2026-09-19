def solution(str1, str2):
    answer = 2
    arr = list(str1)
    k = len(str2)
    window = arr[:k]
    
    if window == list(str2):
        answer = 1
    
    for i in range(k, len(arr)):
        window.pop(0)
        window.append(arr[i])    
        
        if window == list(str2):
            answer = 1
            break
        
    return answer