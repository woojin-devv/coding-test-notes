N = int(input())

def solution(n):
    if n <= 0:
        return 0

    return n + solution(n - 2)

print(solution(N))