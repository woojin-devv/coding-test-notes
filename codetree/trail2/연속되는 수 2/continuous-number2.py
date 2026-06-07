n = int(input())
arr = [int(input()) for _ in range(n)]

cnt = 0 
cnts = []
for i in range(n):
    if arr[i] != arr[i-1] or i == 0 :
        cnt = 0
    cnt += 1
    cnts.append(cnt)

print(max(cnts))