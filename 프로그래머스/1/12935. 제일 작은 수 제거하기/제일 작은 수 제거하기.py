def solution(arr):
    answer = []
    
    if len(arr) <= 1:
        answer = [-1]
    else: 
        _min = min(arr)
        arr.remove(_min)
        answer = arr
    
    return answer