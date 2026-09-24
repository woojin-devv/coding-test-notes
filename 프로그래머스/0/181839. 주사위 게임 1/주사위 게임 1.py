def solution(a, b):
    answer = 0
    
    if (a + b) % 2 == 0 :
        if a * b % 2 == 0:
            answer = abs(a-b)
        else: answer = pow(a, 2) + pow(b, 2)

    else:
        answer = 2 *(a+b)
    
    return answer

# a = 1, b = 1 -> a + b = 2 (짝)
# a = 2, b = 2 -> a + b = 4 (짝)
# a = 1, b = 2 -> a + b = 3 (홀)
