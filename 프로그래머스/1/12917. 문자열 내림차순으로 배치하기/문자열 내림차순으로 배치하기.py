def solution(s):
    answer = ''
    arr = list(s)
    arr.sort(reverse=True)
    answer = ''.join(arr)
    return answer