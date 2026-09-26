def solution(cipher, code):
    answer = ''
    
    for i, ch in enumerate(cipher):
        if (i+1) % code == 0:
            answer += ch

    return answer