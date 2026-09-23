def solution(my_string, target):
    answer = 0
    k = len(target)
    arr = list(my_string)
    window = arr[:k]
    
    if ''.join(window) == target:
        return 1
    else:
        for i in range(k, len(my_string)):
            window.pop(0)
            window.append(arr[i])
            
            if ''.join(window) == target:
                return 1
        return 0