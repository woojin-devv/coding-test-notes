def solution(a, b):
    def func(a, b):
        temp = ''
        temp += str(a)
        temp += str(b)
        return int(temp)
    num = func(a, b)
    
    if num > 2 * a * b:
        return num
    else:
        return 2 * a * b