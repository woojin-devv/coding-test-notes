def solution(num_list):
    answer = 0
    odd = ''
    even = ''
    for el in num_list:
        if el % 2 == 0:
            even += str(el)
        else:
            odd += str(el)
    
    return int(even) + int(odd)