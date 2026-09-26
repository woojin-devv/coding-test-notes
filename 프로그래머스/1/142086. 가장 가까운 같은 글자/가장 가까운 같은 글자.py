def solution(s):
    answer = []
    arr = list(s)
    d = dict()
    
    for i in range(len(s)):
        if not arr[i] in d:
            d[arr[i]] = i
            answer.append(-1)
        else:
            num = d[arr[i]]
            answer.append(i - num)
            d[arr[i]] = i
        
    return answer