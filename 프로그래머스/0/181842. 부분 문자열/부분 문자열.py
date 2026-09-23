def solution(str1, str2):
    answer = 0
    k = len(str1)
    arr = list(str2)
    
    window = arr[:k]
    
    if ''.join(window) == str1:
        return 1
    
    for i in range(k, len(arr)):
        window.pop(0)
        window.append(arr[i])
        
        if ''.join(window) == str1:
            return 1
    
    return 0