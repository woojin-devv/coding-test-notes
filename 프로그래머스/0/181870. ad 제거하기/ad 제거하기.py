def solution(strArr):
    answer = []
    
    for ch in strArr:
        if "ad" in ch:
            continue
        else:
            answer.append(ch)
            
    return answer