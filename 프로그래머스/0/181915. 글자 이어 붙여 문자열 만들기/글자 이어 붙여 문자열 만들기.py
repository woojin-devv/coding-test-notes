def solution(my_string, index_list):
    answer = ''
    arr = list(my_string)
    for i in index_list:
        answer += my_string[i]
    return answer