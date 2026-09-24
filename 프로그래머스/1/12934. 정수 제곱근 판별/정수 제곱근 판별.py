import math as m

def solution(n):
    root = int(m.sqrt(n))
    if root * root == n:
        return (root + 1) ** 2
    return -1

#sqrt() 함수 사용할 경우 소수점 8번째 자리수 까지 반환