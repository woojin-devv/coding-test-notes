def solution(myString):
    answer = ''
    
    for ch in myString:
        if ch == 'a' or ch == 'A':
            answer += ch.upper()
        else:
            answer += ch.lower()
    
    return answer