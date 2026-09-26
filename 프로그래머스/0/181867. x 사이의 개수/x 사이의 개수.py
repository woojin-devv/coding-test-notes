def solution(myString):
    answer = []
    arr = myString.split('x')
    for ch in arr:
        answer.append(len(ch))
    return answer