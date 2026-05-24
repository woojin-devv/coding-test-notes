n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def _func(arr):
    for i in range(len(arr)):
        if arr[i] < 0 :
            arr[i] *= -1
    return arr

print(*_func(arr))