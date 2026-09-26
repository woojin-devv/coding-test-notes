def solution(arr, intervals):
    answer = []
    
    for el in intervals:
        start = el[0] 
        end = el[1]
        
        for i in range(start, end+1):
            answer.append(arr[i])
            
    return answer