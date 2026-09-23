def solution(myString, pat):
    answer = 0
    k = len(pat)
    
    # 모두 소문자로 초기화 
    myString = myString.lower()
    pat = pat.lower()
    
    print(f"{myString}, {pat}")
    
    arr = list(myString)
    # window 
    window = arr[:k]
    temp = ''.join(window)
    
    if temp == pat:
        answer = 1
        return answer
    else:
        for i in range(k, len(arr)):
            window.pop(0)
            window.append(arr[i])
            
            temp = ''.join(window)
            if temp == pat:
                answer = 1
                return answer
    
    return answer