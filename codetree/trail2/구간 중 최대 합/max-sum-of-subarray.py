n, k = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:k])

_max = window

for i in range(k, n):
    window += arr[i] - arr[i-k]
    if _max < window:
        _max = window

print(_max)

