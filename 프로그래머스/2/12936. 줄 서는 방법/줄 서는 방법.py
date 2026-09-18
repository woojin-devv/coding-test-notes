from math import factorial

def solution(n, k):
    answer = []
    people = list(range(1, n+1))
    
    k -= 1 # 0부터
    
    for i in range(n, 0, -1):
        block = factorial(i - 1)

        idx = k // block

        answer.append(people.pop(idx))
        
        k %= block
    return answer