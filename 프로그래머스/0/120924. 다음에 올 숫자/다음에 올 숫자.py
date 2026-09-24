def solution(common):
    answer = 0
    
    if(common[1] - common[0] == common[2] - common[1]):
        d = common[1] - common[0]
        answer = common[-1] + d
    else:
        l = common[1] // common[0]
        answer = common[-1] * l
    return answer