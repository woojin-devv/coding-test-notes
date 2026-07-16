def solution(n):
    cnt = 1 

    for i in range(n - 1, 1, -1):
        result = n

        for j in range(i, 0, -1):
            result -= j

            if result < 0:
                break

            if result == 0:
                cnt += 1
                break

    return cnt