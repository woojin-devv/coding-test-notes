from collections import Counter as counter
n, k = map(int, input().split())
arr = list(map(int, input().split()))


freq = counter(arr)
freq = sorted(freq.items(), key=lambda x: (-x[1], -x[0]))

for i in range(k):
    print(freq[i][0], end=" ")