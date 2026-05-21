n = int(input())

# Please write your code here.
def _function(n):
    hap = 0
    for i in range(1, n+1):
        hap += i
    
    return print(hap // 10)

_function(n)