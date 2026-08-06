n = int(input())
a, b, c = map(int, input().split())

total = n * n * n 
cnt = 0 

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            if abs(a - i) > 2 and abs(b - j) > 2 and abs(c-k) > 2:
                cnt += 1
print(total - cnt)
