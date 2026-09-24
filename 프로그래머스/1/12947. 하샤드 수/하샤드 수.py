def solution(x):
    sum = 0
    answer =0
    arr = [int(digit) for digit in str(x)]
    
    for i in arr:
        sum += i
        
    print(sum)
    
    if x % sum == 0 : 
        answer = True
    else:
        answer = False
    return answer