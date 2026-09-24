def solution(l, r):
    answer = []
    for i in range(l, r+1): 
        for j in str(i):
            if j != '0' and j != '5':
                break
        else: answer.append(i)
    return answer if answer else [-1]