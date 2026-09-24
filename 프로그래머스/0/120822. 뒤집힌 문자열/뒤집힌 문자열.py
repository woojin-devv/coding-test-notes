def solution(my_string):
    answer = ''
    answer_arr = [i for i in my_string]
    for _ in range(len(my_string)):
        answer += answer_arr.pop()
    return answer