def solution(n):

    #Int to Array 
    arr = [int(digit) for digit in str(n)]
    #Array Sorted
    sorted_list = sorted(arr, reverse=True)
    # Array to Int
    sorted_num = int(''.join(map(str, sorted_list)))
    #return Int
    return sorted_num