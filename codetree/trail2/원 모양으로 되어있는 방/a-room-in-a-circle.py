n = int(input())
a = [int(input()) for _ in range(n)]

# 거리의 합
min_answer = float('inf')

# i는 시작하는 방 번호
for i in range(n):
    visited = [False] * n

    # 첫 번째 방 방문 처리 
    visited[i] = True

    temp = 0
    cnt = 1
    while True:
        i = (i + 1) % n
        if visited[i]:
            break
        # 방문 처리
        visited[i] = True
        temp += cnt * a[i]
        cnt += 1

    min_answer = min(min_answer, temp)

print(min_answer)