n, m = map(int, input().split())
A = list(map(int, input().split()))

def solution(m, A):
    result = 0
    while m > 1:
        result += A[m - 1]
        if m % 2 != 0:
            m -= 1
        else:
            m //= 2
    result += A[0]

    return result

print(solution(m, A))
        
