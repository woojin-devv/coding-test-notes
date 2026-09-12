def solution(land):
    answer = 0
    
    for i in range(1, len(land)):
        for j in range(4):
            
            prev = []
            
            for k in range(4):
                if j != k:
                    prev.append(land[i - 1][k])
            land[i][j] += max(prev)
            
            
    return max(land[-1])