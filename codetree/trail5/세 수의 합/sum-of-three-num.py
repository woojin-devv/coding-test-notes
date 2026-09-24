n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0

for i in range(n):
    seen = {}

    for j in range(i + 1, n):
        target = k - arr[i] - arr[j]

        if target in seen:
            answer += seen[target]

        seen[arr[j]] = seen.get(arr[j], 0) + 1

print(answer)