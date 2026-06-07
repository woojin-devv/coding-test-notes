a = input() #이진수 

# a = 111 일 때, a의 최댓값 = 
# a = 10 일 때, 
# a = 0 일 때, => a의 최댓값 = 1 

def extraord(a):
    arr = list(str(a))
    _sum = sum(int(el) for el in arr)
# 0. a = 0 일 때, 
    if a == 0:
        return ['1']

# 1. a의 값이 모두 1일 때, 
    elif (len(arr) == _sum):
        arr[-1] = '0'
        return arr
# 아닌 나머지 => 1이 아닌 가장 앞에 있는 0 -> 1로 변경
    else:
        for i in range(len(arr)):
            if arr[i] == '0':
                arr[i] = '1'
                break
        return arr
# 1010 
# 3210
def binary_to_dec(arr):
    #num은 arr
    result = 0
    # 3, 2, 1, 0
    for i in range(len(arr)-1, -1, -1):
        result += (int(arr[len(arr)-i-1]) * pow(2, i))

    return result

print(binary_to_dec(extraord(a)))