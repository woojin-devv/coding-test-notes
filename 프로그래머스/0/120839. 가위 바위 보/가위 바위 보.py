def solution(rsp):
    answer = ''
    # 가위 - 2, 바위 - 0, 보 - 5
    
    # 2 -> 0
    # 0 -> 5 
    # 5 -> 2
    
    arr = list(rsp)

    for el in arr:
        if int(el) == 2:
            answer += '0'
        elif int(el) == 0:
            answer += '5'
        else: 
            answer += '2'
    return answer