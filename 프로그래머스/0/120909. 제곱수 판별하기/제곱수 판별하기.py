def solution(n):
    temp = int(n ** 0.5)

    if temp * temp == n:
        return 1
    return 2