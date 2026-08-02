N, B = map(int, input().split())
P = [int(input()) for _ in range(N)]

P.sort()

max_student = 0

# i는 반값으로 선물을 줄 학생
for i in range(N):
    total = P[i] // 2

    if total > B:
        continue

    c_student = 1

    for j in range(N):
        if i == j:
            continue

        if total + P[j] <= B:
            total += P[j]
            c_student += 1
        else:
            break

    max_student = max(max_student, c_student)

print(max_student)