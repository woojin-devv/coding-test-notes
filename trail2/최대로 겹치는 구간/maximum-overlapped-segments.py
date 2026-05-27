n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

OFFSET = 100
MAX_SIZE = 201
results = [0] * MAX_SIZE

for i in range(n):
    x, y = segments[i]

    x += OFFSET
    y += OFFSET

    for j in range(x, y):
        results[j] += 1

print(max(results))
