def solution(arr):
    tot_sum = 0
    
    for i in arr:
        tot_sum += i
    
    avg = tot_sum / len(arr)
    
    return avg