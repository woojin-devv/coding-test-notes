a, b = map(int, input().split())

def p_num(n):
    if n % 2 == 0 or n % 5 == 0 :
        return False
    elif n % 3 == 0 and n % 9 != 0:
        return False
    return True

count = 0 
for i in range(a, b+1):
    if p_num(i):
        count += 1

print(count)