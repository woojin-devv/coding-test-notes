def solution(num, k):
    target = str(k)

    for i, ch in enumerate(str(num), start=1):
        if ch == target:
            return i

    return -1