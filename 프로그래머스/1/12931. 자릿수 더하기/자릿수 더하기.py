def solution(n):
    answer = 0
    s = str(n)
    
    for ch in s:
        answer += int(ch)
    return answer