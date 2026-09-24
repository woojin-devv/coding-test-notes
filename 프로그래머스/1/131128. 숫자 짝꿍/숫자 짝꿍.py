from collections import Counter

def solution(X, Y):
    count_X = Counter(str(X))
    count_Y = Counter(str(Y))
    
    result = []
    for digit in map(str, range(9, -1, -1)):
        if digit in count_X and digit in count_Y:
            result.append(digit * min(count_X[digit], count_Y[digit]))
    
    if not result:
        return "-1"
    
    result_str = ''.join(result)
    return "0" if result_str[0] == "0" else result_str
