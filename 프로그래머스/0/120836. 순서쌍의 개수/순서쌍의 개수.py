def solution(n):
    answer = 0
    temp = []
    for i in range(1, n+1):
        if n % i == 0 :
            temp.append(i)
    answer = len(temp)
    return answer