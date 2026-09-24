def count_divisors(n):
    cnt = 0

    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            cnt += 1 if i * i == n else 2

    return cnt

def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if count_divisors(i) % 2 == 0:
            answer += i
        else: 
            answer -= i
    return answer