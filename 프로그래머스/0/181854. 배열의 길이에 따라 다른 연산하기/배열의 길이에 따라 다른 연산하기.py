def solution(arr, n):
    answer = []
    if len(arr) % 2 == 0:
        for i in range(len(arr)):
            if i % 2 != 0:
                arr[i] += n
        answer = arr
                        
    else:
        for i in range(len(arr)):
            if i % 2 == 0:
                arr[i] += n
        answer = arr
    return answer