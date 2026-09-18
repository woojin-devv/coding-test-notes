def solution(my_string):
    answer = ''
    vowels = ['a', 'e', 'i', 'o', 'u']
    
    temp = list(my_string)
    
    for el in temp:
        if el not in vowels:
            answer += el

    return answer