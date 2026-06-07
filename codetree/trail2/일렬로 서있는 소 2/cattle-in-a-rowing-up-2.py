N = int(input())
A = list(map(int, input().split()))

# 5
# 1 2 3 4 5 
# 3 1 7 10 4

# 경우의 수 1
# 
cnt = 0
for i in range(N):
    curr = A[i]
    for j in range(i+1, N):
        if A[j] >= curr:
            for l in range(j+1, N):
                if A[l] >= A[j]:
                    cnt += 1

print(cnt)