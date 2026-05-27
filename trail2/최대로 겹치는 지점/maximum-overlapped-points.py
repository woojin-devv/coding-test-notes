n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

MAX_SIZE = 101

results = [0] * MAX_SIZE

for i in range(n):
    x, y = segments[i]

    for j in range(x, y+1):
        results[j] += 1

print(max(results))