N = int(input())

def factorial(N):
    if N == 0 or N == 1:
        return 1
    
    return N * factorial(N-1)

answer = factorial(N)

print(answer)