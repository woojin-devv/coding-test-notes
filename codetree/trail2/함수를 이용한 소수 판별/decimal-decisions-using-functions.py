a, b = map(int, input().split())

# Please write your code here.

def is_prime(n):
    if n < 2 :
        return False
    else:
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
                break
    return True

result = 0
for i in range(a, b+1):
    if is_prime(i):
        result += i

print(result)