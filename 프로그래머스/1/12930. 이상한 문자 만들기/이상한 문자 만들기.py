def solution(s):
    answer = ''
    arr = s.split(' ')

    for el in arr:
        arr2 = list(el)

        for i in range(len(arr2)):
            if i % 2 == 0:
                answer += arr2[i].upper()
            else:
                answer += arr2[i].lower()

        answer += ' '

    return answer[:-1]