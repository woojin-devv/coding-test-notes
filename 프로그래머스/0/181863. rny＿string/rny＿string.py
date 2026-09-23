def solution(rny_string):
    arr = list(rny_string)
    
    for i in range(len(rny_string)):
        if arr[i] == 'm':
            arr[i] = 'rn'
    
    return ''.join(arr)