def solution(s):
    s = list(s)
    answer = ''
    idx = 0
    if len(s) % 2 == 0:
        idx = len(s) // 2
        answer += s[idx - 1]
        answer += s[idx]
    else:
        idx = len(s) // 2
        answer = (s[idx])
    return answer