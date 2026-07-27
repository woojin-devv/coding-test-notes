n = int(input())
S = input()

cnt = 0
# i는 C의 위치
for i in range(n):
    for j in range(i, n):
        for w in range(j, n):
            if S[i] == 'C' and S[j] == 'O' and S[w] == 'W':
                cnt += 1 

print(cnt)