def solution(arr1, arr2):
    answer = 0
    sum_1 = 0 
    sum_2 = 0 
    if len(arr1) == len(arr2):
        for i in arr1:
            sum_1 += i
        for i in arr2:
            sum_2 += i
        
        if sum_1 > sum_2:
            return 1
        if sum_1 < sum_2:
            return -1
        else:
            return 0
    elif len(arr1) > len(arr2):
        return 1
    elif len(arr1) < len(arr2):
        return -1
    return answer