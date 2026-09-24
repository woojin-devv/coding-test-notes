from collections import Counter as c

n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

freq = c(arr)

for el in nums: 
    print(freq[el], end=" ")

    