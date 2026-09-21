# 완전 탐색 풀이 
def solution(t, p):
    answer = 0
    temp = []
    
    # 문자열 -> list
    arr = list(t)
    k = len(p)
    
    window = arr[:k]
    s = ''.join(window)
    temp.append(s)
    
    for i in range(k, len(arr)):
        window.pop(0)
        window.append(arr[i])
        s = ''.join(window)
        temp.append(s)
    
    for el in temp:
        if int(el) <= int(p):
            answer += 1
    
    return answer