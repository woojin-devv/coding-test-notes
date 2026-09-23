def solution(arr):
    answer = []
    start = 0 
    for el in arr:
        for _ in range(start, start + el):
            answer.append(el)
    return answer