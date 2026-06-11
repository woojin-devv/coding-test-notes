N = int(input())

def solution(N):
    if N == 1:
        return 1
    elif N == 2:
        return 1
    else:
        return solution(N-1) + solution(N-2)

print(solution(N))

# n = 0, 0
# n = 1, 1
# n = 2, 1
# n = 3, 2
# n = 4, 3
# n = 5, 5
