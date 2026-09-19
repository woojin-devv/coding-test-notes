def solution(price, money, count):
    answer = -1
    temp = 0
    for n in range(1, count+1):
        temp += n * price
    
    if money >= temp:
        answer = 0
    else:
        answer = abs(money - temp)
    return answer