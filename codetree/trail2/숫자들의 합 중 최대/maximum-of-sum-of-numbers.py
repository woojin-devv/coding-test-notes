X, Y = map(int, input().split())

_max = 0

for i in range(X, Y+1):
    temp = 0
    for el in list(str(i)):
        temp += int(el)
    
    if _max < temp:
        _max = temp

print(_max)