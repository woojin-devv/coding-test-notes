def solution(s):
    answer = []
    d = {}

    for i, ch in enumerate(s):
        if ch not in d:
            answer.append(-1)
        else:
            answer.append(i - d[ch])

        d[ch] = i

    return answer