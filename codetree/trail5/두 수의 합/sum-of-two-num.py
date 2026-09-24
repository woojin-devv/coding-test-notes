n, k = map(int, input().split())
arr = list(map(int, input().split()))

seen = {}
answer = 0

for el in arr:
    target = k - el

    if target in seen:
        answer += seen[target]

    seen[el] = seen.get(el, 0) + 1

print(answer)