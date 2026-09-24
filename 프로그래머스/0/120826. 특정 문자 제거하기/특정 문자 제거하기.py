def solution(my_string, letter):
    answer = ''
    
    for el in my_string:
        if el != letter:
            answer += el
            
    return answer