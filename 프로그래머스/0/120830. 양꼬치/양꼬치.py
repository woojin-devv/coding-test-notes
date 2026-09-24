def solution(n, k):
    answer = 0
    service = n // 10
    drink = k - service
    
    answer = (n * 12000) + (drink * 2000)
    return answer