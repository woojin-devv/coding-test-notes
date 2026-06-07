from math import sqrt


a, b = map(int, input().split())

def is_prime(num):
    if num < 2:
        return False 

    for i in range(2, int(sqrt(num))+1):
        if num % i == 0:
            return False
    return True

def is_sum_even(num):
    result = 0
    arr = list(str(num))
    for el in arr:
        result += int(el)
    
    if result % 2 == 0:
        return True
    
    return False

cnt = 0
for i in range(a, b+1):
    if is_prime(i) and is_sum_even(i):
        cnt += 1
    
print(cnt)
    
    