from collections import Counter

def solution(want, number, discount):
    cnt = 0
    k = 10
    
    wants = dict(zip(want, number))
    
    # number의 원소의 합은 항상 10임. 
    # discount 중 slice 10으로 want랑 number 가 있는지 확인 -> 있으면 count +=1 
    
    # 첫 slice
    window = discount[:k]
    
    if Counter(window) == wants:
        cnt += 1
    
    for idx in range(k, len(discount)):
        window.pop(0)
        window.append(discount[idx])
        
        if Counter(window) == wants:
            cnt += 1
    
    return cnt