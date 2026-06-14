N, M, K = map(int, input().split())
student = [0] * (N+1) # 1번부터 카운팅 하기 위해

# i는 벌금 
result = -1
for i in range(M):
    target = int(input())

    student[target] += 1

    if student[target] >= K:
        result = target
        break

print(result)