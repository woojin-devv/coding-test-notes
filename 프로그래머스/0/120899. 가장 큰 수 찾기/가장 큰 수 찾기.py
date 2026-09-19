def solution(arr):
    max_value = -1
    max_index = -1

    for i in range(len(arr)):
        if max_value < arr[i]:
            max_value = arr[i]
            max_index = i

    return [max_value, max_index]