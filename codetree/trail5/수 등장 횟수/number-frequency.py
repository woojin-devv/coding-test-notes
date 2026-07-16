from collections import Counter as c

n, m = map(int, input().split())
arr = list(map(int, input().split()))
nums = list(map(int, input().split()))

# 완전탐색 풀이 - 시간초과 
# answer = []
# for el in nums:
#     cnt = 0
#     for el2 in arr:
#         if el == el2:
#             cnt += 1
#     answer.append(cnt)

# print(*answer)

# Counter로 개수 

freq = c(arr)

for el in nums:
    print(freq[el], end=" ")