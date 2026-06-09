N = int(input())

def solution(N):
    if N == 1:
        return 0
    else:
        if N % 2 == 0:
            return 1 + solution(N // 2)
        else:
            return 1 + solution(N // 3)
        
print(solution(N))