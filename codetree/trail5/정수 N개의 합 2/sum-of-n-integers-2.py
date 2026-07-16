n, k = map(int, input().split())
arr = list(map(int, input().split()))

window = sum(arr[:k])
answer = window

for i in range(k, len(arr)):
    window += (arr[i] - arr[i-k])
    answer = max(answer, window)

print(answer)