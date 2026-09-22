def solution(n, control):
    answer = n
    arr = list(control)
    
    for el in control:
        if el == 'w':
            answer += 1
        elif el == 's':
            answer -= 1
        elif el == 'd':
            answer += 10
        elif el == 'a':
            answer -= 10
    return answer