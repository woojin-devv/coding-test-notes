def solution(my_string, n):
    answer = ''
    for el in my_string:
        answer += el * n
    return answer